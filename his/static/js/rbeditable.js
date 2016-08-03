(function($) {
	    var Radiolist = function(options) {
	        this.init('radiolist', options, Radiolist.defaults);
	    };
	    $.fn.editableutils.inherit(Radiolist, $.fn.editabletypes.checklist);

	    $.extend(Radiolist.prototype, {
	        renderList : function() {
	            var $label;
	            this.$tpl.empty();
	            if (!$.isArray(this.sourceData)) {
	                return;
	            }

	            for (var i = 0; i < this.sourceData.length; i++) {
	                $label = $('<label>', {'class':this.options.inputclass}).append($('<input>', {
	                    type : 'radio',
	                    name : this.options.name,
	                    value : this.sourceData[i].value
	                })).append($('<span>').text(this.sourceData[i].text));

	                // Add radio buttons to template
	                this.$tpl.append($label);
	            }

	            this.$input = this.$tpl.find('input[type="radio"]');
	        },
	        input2value : function() {
	            return this.$input.filter(':checked').val();
	        },
	        str2value: function(str) {
	           return str || null;
	        },
	        
	        value2input: function(value) {
	           this.$input.val([value]);
	        },
	        value2str: function(value) {
	           return value || '';
	        },
	    });

	    Radiolist.defaults = $.extend({}, $.fn.editabletypes.list.defaults, {
	        /**
	         @property tpl
	         @default <div></div>
	         **/
	        tpl : '<div class="editable-radiolist"></div>',

	        /**
	         @property inputclass, attached to the <label> wrapper instead of the input element
	         @type string
	         @default null
	         **/
	        inputclass : '',

	        name : 'defaultname'
	    });

	    $.fn.editabletypes.radiolist = Radiolist;
	}(window.jQuery));