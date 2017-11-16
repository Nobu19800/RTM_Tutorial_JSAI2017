/**
 * theme935 javascript core
 *
 * - Provides frequently used extensions to base javascript objects
 * - jQuery browser detection tweak
 * - Define functions used in events
 */

// Add String.trim() method
String.prototype.trim = function() {
	return this.replace(/\s+$/, '').replace(/^\s+/, '');
}

// Add Array.indexOf() method
if (!Array.prototype.indexOf) {
	Array.prototype.indexOf = function (obj, fromIndex) {
		if (fromIndex == null) {
			fromIndex = 0;
		} else if (fromIndex < 0) {
			fromIndex = Math.max(0, this.length + fromIndex);
		}

		for (var i = fromIndex, j = this.length; i < j; i++) {
			if (this[i] === obj) {
				return i;
			}
		}
		return -1;
	};
}

// jQuery Browser Detect Tweak For IE7
jQuery.browser.version = jQuery.browser.msie && parseInt(jQuery.browser.version) == 6 && window["XMLHttpRequest"] ? "7.0" : jQuery.browser.version;

// Console.log wrapper to avoid errors when firebug is not present
// usage: log('inside coolFunc', this, arguments);
// paulirish.com/2009/log-a-lightweight-wrapper-for-consolelog/
window.log = function() {
	log.history = log.history || []; // store logs to an array for reference
	log.history.push(arguments);
	if (this.console) {
		console.log(Array.prototype.slice.call(arguments));
	}
};

// init object
var theme935 = theme935 || {};

/**
 * Image handling functions
 */
theme935.image = { _cache : [] };

// preload images
theme935.image.preload = function() {
	for (var i = arguments.length; i--;) {
		var cacheImage = document.createElement('img');
		cacheImage.src = arguments[i];
		theme935.image._cache.push(cacheImage);
	}
};
jQuery(window).bind('load', function() {
	jQuery('.foreground').toggle('slow');
});

jQuery(function() {
	jQuery('.isotope-element .views-field-field-portfolio-image a').hover(function() {
		jQuery(this).find('img').stop().animate({opacity:'.4'})
	},

	function() {
		jQuery(this).find('img').stop().animate({opacity:'1'})
	})
	
	if (false) //#3912 +
	if (jQuery('html').hasClass('desktop')) {
		jQuery.srSmoothscroll({
			step: 150,
			speed: 800
		});
	}
});

(function($) {
	jQuery(document).ready(function($) {
		if (jQuery(".portfolio-grid").length) {
			var $container = jQuery('#isotope-container'),
				filters = {},
				items_count = jQuery(".isotope-element").size();

			$container.imagesLoaded( function() {
				setColumnWidth();
				$container.isotope({
					itemSelector		: '.isotope-element',
					resizable			: false,
					transformsEnabled	: true,
					layoutMode			: 'fitRows',
				});
			});

			function getNumColumns() {
				var $folioWrapper = jQuery('#isotope-container').data('cols');

				if ($folioWrapper == '1col') {
					var winWidth = jQuery("#isotope-container").width(),
						column = 1;
					return column;
				}

				else if ($folioWrapper == '2cols') {
					var winWidth = jQuery("#isotope-container").width(),
						column = 2;
					if (winWidth < 380) {
						column = 1;
					}
					return column;
				}

				else if ($folioWrapper == '3cols') {
					var winWidth = jQuery("#isotope-container").width(),
						column = 3;
					if (winWidth < 380) {
						column = 1;
					}
					else if ((winWidth >= 380) && (winWidth < 788)) {
						column = 2;
					}
					else if (winWidth >= 788) {
						column = 3;
					}
					return column;
				}

				else if ($folioWrapper == '4cols') {
					var winWidth = jQuery("#isotope-container").width(),
						column = 4;
					if (winWidth < 380) {
						column = 1;
					}
					else if ((winWidth >= 380) && (winWidth < 788)) {
						column = 2;
					}
					else if ((winWidth >= 788) && (winWidth < 940)) {
						column = 3;
					}
					else if (winWidth >= 940) {
						column = 4;
					}
					return column;
				}
			}

			function setColumnWidth() {
				var columns = getNumColumns(),
					containerWidth = jQuery("#isotope-container").width(),
					postWidth;

				if (columns == 1) {
					postWidth = containerWidth - 20;
				}
				if (columns == 2) {
					postWidth = (containerWidth - 40)/columns;
				}
				if (columns == 3) {
					postWidth = (containerWidth - 60)/columns;
				}
				if (columns == 4) {
					postWidth = (containerWidth - 80)/columns;
				}

				postWidth = Math.floor(postWidth);

				jQuery(".isotope-element").each(function(index) {
					jQuery(this).css({"width" : postWidth + "px"});
				});
			}

			function arrange() {
				setColumnWidth();
				$container.isotope('reLayout');
			}

			jQuery(window).on("debouncedresize", function(event) {
				arrange();
			});
		};

		if ($.cookie('the_cookie') == 0) {
			styleSwitch(0)
		}

		function styleSwitch(cookie) {
			if (cookie == 0) {
				$('#style-mobile').remove();
				$('#skeleton-mobile').remove();
				$('.switcher').text("Responsive Version");
				$.cookie('the_cookie', 0);
			} else {
				$('head').append('<link rel="stylesheet" href="<?php echo base_path().path_to_theme() ?>/css/style-mobile.css" media="screen" id="style-mobile">');
				$('head').append('<link rel="stylesheet" href="<?php echo base_path().path_to_theme() ?>/css/skeleton-mobile.css" media="screen" id="skeleton-mobile">');
				$('.switcher').text("Desktop Version only");
				$.cookie('the_cookie', 1);
			}
		}

		$('.switcher').click(function() {
			styleSwitch($.cookie('the_cookie') == 0 ? 1 : 0);
			location.reload();
		});
	});
})(jQuery);

jQuery(document).ready(function () {
	jQuery("#isotope-options .option-set li a[data-option-value='.all']").addClass("selected");
	
	// Sticky menu
	if ((jQuery(window).width() > 995) && (jQuery('#header .stickup').length)) {
		jQuery('#header .stickup').tmStickUp({});
	}
	
	// Portfolio image size
	jQuery('.tm-masonry-item img').each(function() {
		var width = jQuery(this).parents('.tm-masonry-item').width(),
			height = jQuery(this).parents('.tm-masonry-item').height(),
			h = height/width;
		
		if (h > 0.5194) {
			jQuery(this).css({height: height, maxWidth: 'inherit'});
		} else {
			jQuery(this).css({height: 'auto', maxWidth: '100%'});
		}
	})
	
	// Contact form validation
	var my_form_id = new tFormer('contact-site-form', {
		fields: {
			name: {
				rules: "*"
			},
			mail: {
				rules: "* @"
			},
			subject: {
				rules: "*"
			},
			message: {
				rules: "*"
			}
		}
	});
	
	// Contact form tooltips
	jQuery(".contact-form label[for='edit-name']").attr('data-title', 'Enter your name here');
	jQuery(".contact-form label[for='edit-mail']").attr('data-title', 'Enter your contact Email here');
	jQuery(".contact-form label[for='edit-subject']").attr('data-title', 'Enter the subject of your message here');
	jQuery(".contact-form label[for='edit-message']").attr('data-title', 'Enter your message here');
	jQuery(".contact-form label[for='edit-copy']").attr('data-title', 'Check to send coty to yourself');
	jQuery(".contact-form .form-item-name").append('<div class="messages error">This field is required!</div>');
	jQuery(".contact-form .form-item-mail").append('<div class="messages error">This field is required!<br>Please enter a valid email address!</div>');
	jQuery(".contact-form .form-item-subject").append('<div class="messages error">This field is required!</div>');
	jQuery(".contact-form .form-item-message .form-textarea-wrapper").append('<div class="messages error">This field is required!</div>');
	jQuery(".btn a,.more-link a").wrap('<span></span>');
});

// Tiled gallery
jQuery(window).bind('resize', function() {
	jQuery('.tm-masonry-item img').each(function() {
		var width = jQuery(this).parents('.tm-masonry-item').width(),
			height = jQuery(this).parents('.tm-masonry-item').height(),
			h = height/width;
		
		if (h > 0.5194) {
			jQuery(this).css({height: height, maxWidth: 'inherit'});
		} else {
			jQuery(this).css({height: 'auto', maxWidth: '100%'});
		}
	})
})

// Back to Top Button
jQuery(window).load(function() {
	jQuery().UItoTop({
		easingType: 'easeOutQuart',
		containerID: 'backtotop'
	});
})

// Mobile menu
jQuery(window).load(function() {
	jQuery('#superfish-1').mobileMenu();
})
;
/*
 * debouncedresize: special jQuery event that happens once after a window resize
 *
 * latest version and complete README available on Github:
 * https://github.com/louisremi/jquery-smartresize
 *
 * Copyright 2012 @louis_remi
 * Licensed under the MIT license.
 *
 * This saved you an hour of work?
 * Send me music http://www.amazon.co.uk/wishlist/HNTU0468LQON
 */
(function($) {
	var $event = $.event,
		$special,
		resizeTimeout;

	$special = $event.special.debouncedresize = {
		setup: function() {
			$(this).on("resize", $special.handler);
		},
		teardown: function() {
			$(this).off("resize", $special.handler);
		},
		handler: function(event, execAsap) {
			// Save the context
			var context = this,
				args = arguments,
				dispatch = function() {
					// set correct event type
					event.type = "debouncedresize";
					$event.dispatch.apply(context, args);
				};

			if (resizeTimeout) {
				clearTimeout(resizeTimeout);
			}

			execAsap ?
				dispatch() :
				resizeTimeout = setTimeout( dispatch, $special.threshold );
		},
		threshold: 150
	};
})(jQuery);;
/**
 * jQuery Mobile Menu 
 * Turn unordered list menu into dropdown select menu
 * version 1.1(27-JULY-2013)
 * 
 * Built on top of the jQuery library
 *   http://jquery.com
 * 
 * Documentation
 * 	 http://github.com/mambows/mobilemenu
 */
(function($) {
	$.fn.mobileMenu = function(options) {
		var defaults = {
			defaultText		: 'Navigate to...',
			className		: 'select-menu',
			subMenuClass	: 'sub-menu',
			subMenuDash		: '&ndash;',
		},
		settings =	$.extend(defaults, options),
					el = $(this);
		
		this.each(function(){
			var $el = $(this),
				$select_menu;
	
			// ad class to submenu list
			$el.find('ul').addClass(settings.subMenuClass);
	
			// Create base menu
			var $select_menu = $('<select />', {
				'class' : settings.className + ' ' + el.get(0).className
			}).insertAfter( $el );
	
			// Create default option
			$('<option />', {
				"value"		: '#',
				"text"		: settings.defaultText
			}).appendTo( $select_menu );
	
			// Create select option from menu
			$el.find('a').each(function(){
				var $this 	= $(this),
					optText	= '&nbsp;' + $this.text(),
					optSub	= $this.parents('.' + settings.subMenuClass),
					len		= optSub.length,
					dash;
				
				// if menu has sub menu
				if ($this.parents('ul').hasClass(settings.subMenuClass)) {
					dash = Array(len + 1).join(settings.subMenuDash);
					optText = dash + optText;
				}
	
				// Now build menu and append it
				$('<option />', {
					"value"	: this.href,
					"html"	: optText,
					"selected" : (this.href == window.location.href)
				}).appendTo($select_menu);
	
			}); // End el.find('a').each
	
			// Change event on select element
			$select_menu.change(function(){
				var locations = $(this).val();
				if (locations !== '#') {
					window.location.href = $(this).val();
				};
			});
		}); // End this.each
		return this;
	};
})(jQuery);;
/*
 * jQuery Easing v1.3 - http://gsgd.co.uk/sandbox/jquery/easing/
 *
 * Uses the built in easing capabilities added In jQuery 1.1
 * to offer multiple easing options
 *
 * TERMS OF USE - jQuery Easing
 * 
 * Open source under the BSD License. 
 * 
 * Copyright © 2008 George McGinley Smith
 * All rights reserved.
 * 
 * Redistribution and use in source and binary forms, with or without modification, 
 * are permitted provided that the following conditions are met:
 * 
 * Redistributions of source code must retain the above copyright notice, this list of 
 * conditions and the following disclaimer.
 * Redistributions in binary form must reproduce the above copyright notice, this list 
 * of conditions and the following disclaimer in the documentation and/or other materials 
 * provided with the distribution.
 * 
 * Neither the name of the author nor the names of contributors may be used to endorse 
 * or promote products derived from this software without specific prior written permission.
 * 
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY 
 * EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
 * MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
 *  COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
 *  EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE
 *  GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED 
 * AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
 *  NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED 
 * OF THE POSSIBILITY OF SUCH DAMAGE. 
 *
*/

// t: current time, b: begInnIng value, c: change In value, d: duration
jQuery.easing['jswing'] = jQuery.easing['swing'];

jQuery.extend( jQuery.easing,
{
	def: 'easeOutQuad',
	swing: function (x, t, b, c, d) {
		//alert(jQuery.easing.default);
		return jQuery.easing[jQuery.easing.def](x, t, b, c, d);
	},
	easeInQuad: function (x, t, b, c, d) {
		return c*(t/=d)*t + b;
	},
	easeOutQuad: function (x, t, b, c, d) {
		return -c *(t/=d)*(t-2) + b;
	},
	easeInOutQuad: function (x, t, b, c, d) {
		if ((t/=d/2) < 1) return c/2*t*t + b;
		return -c/2 * ((--t)*(t-2) - 1) + b;
	},
	easeInCubic: function (x, t, b, c, d) {
		return c*(t/=d)*t*t + b;
	},
	easeOutCubic: function (x, t, b, c, d) {
		return c*((t=t/d-1)*t*t + 1) + b;
	},
	easeInOutCubic: function (x, t, b, c, d) {
		if ((t/=d/2) < 1) return c/2*t*t*t + b;
		return c/2*((t-=2)*t*t + 2) + b;
	},
	easeInQuart: function (x, t, b, c, d) {
		return c*(t/=d)*t*t*t + b;
	},
	easeOutQuart: function (x, t, b, c, d) {
		return -c * ((t=t/d-1)*t*t*t - 1) + b;
	},
	easeInOutQuart: function (x, t, b, c, d) {
		if ((t/=d/2) < 1) return c/2*t*t*t*t + b;
		return -c/2 * ((t-=2)*t*t*t - 2) + b;
	},
	easeInQuint: function (x, t, b, c, d) {
		return c*(t/=d)*t*t*t*t + b;
	},
	easeOutQuint: function (x, t, b, c, d) {
		return c*((t=t/d-1)*t*t*t*t + 1) + b;
	},
	easeInOutQuint: function (x, t, b, c, d) {
		if ((t/=d/2) < 1) return c/2*t*t*t*t*t + b;
		return c/2*((t-=2)*t*t*t*t + 2) + b;
	},
	easeInSine: function (x, t, b, c, d) {
		return -c * Math.cos(t/d * (Math.PI/2)) + c + b;
	},
	easeOutSine: function (x, t, b, c, d) {
		return c * Math.sin(t/d * (Math.PI/2)) + b;
	},
	easeInOutSine: function (x, t, b, c, d) {
		return -c/2 * (Math.cos(Math.PI*t/d) - 1) + b;
	},
	easeInExpo: function (x, t, b, c, d) {
		return (t==0) ? b : c * Math.pow(2, 10 * (t/d - 1)) + b;
	},
	easeOutExpo: function (x, t, b, c, d) {
		return (t==d) ? b+c : c * (-Math.pow(2, -10 * t/d) + 1) + b;
	},
	easeInOutExpo: function (x, t, b, c, d) {
		if (t==0) return b;
		if (t==d) return b+c;
		if ((t/=d/2) < 1) return c/2 * Math.pow(2, 10 * (t - 1)) + b;
		return c/2 * (-Math.pow(2, -10 * --t) + 2) + b;
	},
	easeInCirc: function (x, t, b, c, d) {
		return -c * (Math.sqrt(1 - (t/=d)*t) - 1) + b;
	},
	easeOutCirc: function (x, t, b, c, d) {
		return c * Math.sqrt(1 - (t=t/d-1)*t) + b;
	},
	easeInOutCirc: function (x, t, b, c, d) {
		if ((t/=d/2) < 1) return -c/2 * (Math.sqrt(1 - t*t) - 1) + b;
		return c/2 * (Math.sqrt(1 - (t-=2)*t) + 1) + b;
	},
	easeInElastic: function (x, t, b, c, d) {
		var s=1.70158;var p=0;var a=c;
		if (t==0) return b;  if ((t/=d)==1) return b+c;  if (!p) p=d*.3;
		if (a < Math.abs(c)) { a=c; var s=p/4; }
		else var s = p/(2*Math.PI) * Math.asin (c/a);
		return -(a*Math.pow(2,10*(t-=1)) * Math.sin( (t*d-s)*(2*Math.PI)/p )) + b;
	},
	easeOutElastic: function (x, t, b, c, d) {
		var s=1.70158;var p=0;var a=c;
		if (t==0) return b;  if ((t/=d)==1) return b+c;  if (!p) p=d*.3;
		if (a < Math.abs(c)) { a=c; var s=p/4; }
		else var s = p/(2*Math.PI) * Math.asin (c/a);
		return a*Math.pow(2,-10*t) * Math.sin( (t*d-s)*(2*Math.PI)/p ) + c + b;
	},
	easeInOutElastic: function (x, t, b, c, d) {
		var s=1.70158;var p=0;var a=c;
		if (t==0) return b;  if ((t/=d/2)==2) return b+c;  if (!p) p=d*(.3*1.5);
		if (a < Math.abs(c)) { a=c; var s=p/4; }
		else var s = p/(2*Math.PI) * Math.asin (c/a);
		if (t < 1) return -.5*(a*Math.pow(2,10*(t-=1)) * Math.sin( (t*d-s)*(2*Math.PI)/p )) + b;
		return a*Math.pow(2,-10*(t-=1)) * Math.sin( (t*d-s)*(2*Math.PI)/p )*.5 + c + b;
	},
	easeInBack: function (x, t, b, c, d, s) {
		if (s == undefined) s = 1.70158;
		return c*(t/=d)*t*((s+1)*t - s) + b;
	},
	easeOutBack: function (x, t, b, c, d, s) {
		if (s == undefined) s = 1.70158;
		return c*((t=t/d-1)*t*((s+1)*t + s) + 1) + b;
	},
	easeInOutBack: function (x, t, b, c, d, s) {
		if (s == undefined) s = 1.70158; 
		if ((t/=d/2) < 1) return c/2*(t*t*(((s*=(1.525))+1)*t - s)) + b;
		return c/2*((t-=2)*t*(((s*=(1.525))+1)*t + s) + 2) + b;
	},
	easeInBounce: function (x, t, b, c, d) {
		return c - jQuery.easing.easeOutBounce (x, d-t, 0, c, d) + b;
	},
	easeOutBounce: function (x, t, b, c, d) {
		if ((t/=d) < (1/2.75)) {
			return c*(7.5625*t*t) + b;
		} else if (t < (2/2.75)) {
			return c*(7.5625*(t-=(1.5/2.75))*t + .75) + b;
		} else if (t < (2.5/2.75)) {
			return c*(7.5625*(t-=(2.25/2.75))*t + .9375) + b;
		} else {
			return c*(7.5625*(t-=(2.625/2.75))*t + .984375) + b;
		}
	},
	easeInOutBounce: function (x, t, b, c, d) {
		if (t < d/2) return jQuery.easing.easeInBounce (x, t*2, 0, c, d) * .5 + b;
		return jQuery.easing.easeOutBounce (x, t*2-d, 0, c, d) * .5 + c*.5 + b;
	}
});

/*
 *
 * TERMS OF USE - EASING EQUATIONS
 * 
 * Open source under the BSD License. 
 * 
 * Copyright © 2001 Robert Penner
 * All rights reserved.
 * 
 * Redistribution and use in source and binary forms, with or without modification, 
 * are permitted provided that the following conditions are met:
 * 
 * Redistributions of source code must retain the above copyright notice, this list of 
 * conditions and the following disclaimer.
 * Redistributions in binary form must reproduce the above copyright notice, this list 
 * of conditions and the following disclaimer in the documentation and/or other materials 
 * provided with the distribution.
 * 
 * Neither the name of the author nor the names of contributors may be used to endorse 
 * or promote products derived from this software without specific prior written permission.
 * 
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY 
 * EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
 * MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
 *  COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
 *  EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE
 *  GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED 
 * AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
 *  NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED 
 * OF THE POSSIBILITY OF SUCH DAMAGE. 
 *
 */;
(function($) {
	$.fn.UItoTop = function(options) {
		var defaults = {
			text: '',
			min: 500,
			scrollSpeed: 800,
			containerID: 'toTop',
			containerHoverID: 'toTopHover',
			easingType: 'linear',
			min_width: parseInt($('body').css("min-width"),10),
			main_width: parseInt($('body').css("min-width"),10)/2
		};

		var settings = $.extend(defaults, options);
		var containerIDhash = '#' + settings.containerID;
		var containerHoverIDHash = '#' + settings.containerHoverID;

		$('body').append('<a href="#" id="' + settings.containerID + '">' + settings.text + '</a>');

		var button_width = parseInt($(containerIDhash).css("width")) + 90
		var button_width_1 = parseInt($(containerIDhash).css("width")) + 20
		var max_width = defaults.min_width + button_width;
		var margin_right_1 = -(defaults.main_width + button_width_1)
		var margin_right_2 = -(defaults.main_width - 20)
		
		function top() {
			if(($(window).width() <= max_width) && ($(window).width() >= defaults.min_width)) {
				$(containerIDhash).stop().animate({marginRight: margin_right_2, right: '50%'});
			} else {
				if($(window).width() <= defaults.min_width) {
					$(containerIDhash).stop().css({marginRight: 0, right: 10})
				} else {
					$(containerIDhash).stop().animate({marginRight: margin_right_1, right: '50%'})
				}
			}
		}
		top()
		$(containerIDhash).hide().click(function() {
			$('html, body').stop().animate({scrollTop: 0}, settings.scrollSpeed, settings.easingType);
			$('#' + settings.containerHoverID, this).stop().animate({'opacity': 0}, settings.inDelay, settings.easingType);
			return false;
		})

		.prepend('<span id="' + settings.containerHoverID + '"></span>')
		.hover(function() {
				$(containerHoverIDHash, this).stop().animate({
					'opacity': 1
				}, 600, 'linear');
			}, function() {
				$(containerHoverIDHash, this).stop().animate({
					'opacity': 0
				}, 700, 'linear');
			});

		$(window).scroll(function() {
			var sd = $(window).scrollTop();
			if(typeof document.body.style.maxHeight === "undefined") {
				$(containerIDhash).css({
					'position': 'absolute',
					'top': $(window).scrollTop() + $(window).height() - 50
				});
			}
			if (sd > settings.min) {
				$(containerIDhash).stop(true, true).fadeIn(600);
			} else {
				$(containerIDhash).fadeOut(800);
			}
		});
		$(window).resize(function() {
			top()
		})
};
})(jQuery);;
/*!
 * jQuery Cookie Plugin v1.4.1
 * https://github.com/carhartl/jquery-cookie
 *
 * Copyright 2013 Klaus Hartl
 * Released under the MIT license
 */
(function (factory) {
	if (typeof define === 'function' && define.amd) {
		// AMD
		define(['jquery'], factory);
	} else if (typeof exports === 'object') {
		// CommonJS
		factory(require('jquery'));
	} else {
		// Browser globals
		factory(jQuery);
	}
}(function ($) {

	var pluses = /\+/g;

	function encode(s) {
		return config.raw ? s : encodeURIComponent(s);
	}

	function decode(s) {
		return config.raw ? s : decodeURIComponent(s);
	}

	function stringifyCookieValue(value) {
		return encode(config.json ? JSON.stringify(value) : String(value));
	}

	function parseCookieValue(s) {
		if (s.indexOf('"') === 0) {
			// This is a quoted cookie as according to RFC2068, unescape...
			s = s.slice(1, -1).replace(/\\"/g, '"').replace(/\\\\/g, '\\');
		}

		try {
			// Replace server-side written pluses with spaces.
			// If we can't decode the cookie, ignore it, it's unusable.
			// If we can't parse the cookie, ignore it, it's unusable.
			s = decodeURIComponent(s.replace(pluses, ' '));
			return config.json ? JSON.parse(s) : s;
		} catch(e) {}
	}

	function read(s, converter) {
		var value = config.raw ? s : parseCookieValue(s);
		return $.isFunction(converter) ? converter(value) : value;
	}

	var config = $.cookie = function (key, value, options) {

		// Write

		if (value !== undefined && !$.isFunction(value)) {
			options = $.extend({}, config.defaults, options);

			if (typeof options.expires === 'number') {
				var days = options.expires, t = options.expires = new Date();
				t.setTime(+t + days * 864e+5);
			}

			return (document.cookie = [
				encode(key), '=', stringifyCookieValue(value),
				options.expires ? '; expires=' + options.expires.toUTCString() : '', // use expires attribute, max-age is not supported by IE
				options.path    ? '; path=' + options.path : '',
				options.domain  ? '; domain=' + options.domain : '',
				options.secure  ? '; secure' : ''
			].join(''));
		}

		// Read

		var result = key ? undefined : {};

		// To prevent the for loop in the first place assign an empty array
		// in case there are no cookies at all. Also prevents odd result when
		// calling $.cookie().
		var cookies = document.cookie ? document.cookie.split('; ') : [];

		for (var i = 0, l = cookies.length; i < l; i++) {
			var parts = cookies[i].split('=');
			var name = decode(parts.shift());
			var cookie = parts.join('=');

			if (key && key === name) {
				// If second argument (value) is a function it's a converter...
				result = read(cookie, value);
				break;
			}

			// Prevent storing a cookie that we couldn't decode.
			if (!key && (cookie = read(cookie)) !== undefined) {
				result[name] = cookie;
			}
		}

		return result;
	};

	config.defaults = {};

	$.removeCookie = function (key, options) {
		if ($.cookie(key) === undefined) {
			return false;
		}

		// Must not alter options, thus extending a fresh object...
		$.cookie(key, '', $.extend({}, options, { expires: -1 }));
		return !$.cookie(key);
	};

}));;
(function($){
	$.fn.tmStickUp = function(options){ 
		
		var getOptions = {
			correctionSelector: $('.correctionSelector')
		}
		$.extend(getOptions, options); 

		var
			_this = $(this),
			_window = $(window),
			_document = $(document),
			thisOffsetTop = 0,
			thisOuterHeight = 0,
			thisMarginTop = 0,
			thisPaddingTop = 0,
			documentScroll = 0,
			pseudoBlock,
			lastScrollValue = 0,
			scrollDir = '',
			tmpScrolled;

		init();
		function init(){
			thisOffsetTop = parseInt(_this.offset().top);
			thisMarginTop = parseInt(_this.css("margin-top"));
			thisOuterHeight = parseInt(_this.outerHeight(true));

			$('<div class="pseudoStickyBlock"></div>').insertAfter(_this);
			pseudoBlock = $('.pseudoStickyBlock');
			pseudoBlock.css({"position": "relative", "display": "block"});
			addEventsFunction();
		}//end init

		function addEventsFunction(){
			_document.on('scroll', function() {
				tmpScrolled = $(this).scrollTop();
					if (tmpScrolled > lastScrollValue) {
						scrollDir = 'down';
					} else {
						scrollDir = 'up';
					}
				lastScrollValue = tmpScrolled;

				correctionValue = getOptions.correctionSelector.outerHeight(true);
				documentScroll = parseInt(_window.scrollTop());

				if (thisOffsetTop - correctionValue < documentScroll) {
					_this.addClass('isStuck');
					_this.css({position: "fixed", top: correctionValue});
					pseudoBlock.css({"height": thisOuterHeight});
				} else {
					_this.removeClass('isStuck');
					_this.css({position: "relative", top: 0});
					pseudoBlock.css({"height": 0});
				}
			}).trigger('scroll');
		}
	}//end tmStickUp function
})(jQuery);
/**
 * tFormer.js - empower your forms
 * http://tjrus.com/tFormer
 * (c) 2013 Vasiliy Zubach (aka TjRus) - http://tjrus.com/
 * tFormer may be freely distributed under the MIT license.
 */

(function ( window, document, undefined ){

	// button types
	var BUTTON_TYPES = ['button', 'submit'];
	// all field types that can be empowered with tFormer
	var FIELD_TYPES = ['text', 'password', 'select-one', 'checkbox', 'textarea', 'range', 'number', 'email', 'hidden', 'file', 'date', 'datetime-local', 'search', 'tel', 'time', 'url', 'month', 'week'];
	// fields that has only 'change' event
	var HAS_CHANGE_EVENT = ['checkbox', 'select-one', 'select', 'file'];
	// fields that has also 'change' event
	var CHANGE_ALSO = ['number', 'date', 'datetime-local', 'time', 'month', 'week', 'range'];

	// tFormer options
	var TF_OPTIONS = ['timeout', 'requestTimeout', 'errorClass', 'disabledClass', 'processingClass', 'validateEvent', 'submitButtonControl', 'submitButton', 'submit', 'before', 'onerror', 'onvalid', 'eventBefore', 'eventError', 'eventValid'];
	var FIELD_OPTIONS = ['timeout', 'requestTimeout', 'request', 'validClass', 'errorClass', 'disabledClass', 'processingClass', 'rules', 'validateEvent', 'before', 'onerror', 'onvalid', 'own', 'eventBefore', 'eventError', 'eventValid'];
	var BUTTON_OPTIONS = ['disabledClass', 'processingClass'];


	var EMPOWERED = 'empowered';

	var defaults = {
		errorClass     : 'error',
		processingClass: 'processing',
		disabledClass  : 'disabled',
		validClass     : 'valid',

		eventBefore: 'tFormer:before',
		eventError : 'tFormer:error',
		eventValid : 'tFormer:valid',

		timeout       : 0,
		requestTimeout: 2000,

		validateEvent: 'input keyup',

		fields : {},
		buttons: {},

		submitButtonControl: true,
		submitButton       : null
	};

	/**
	 * Main tFormer constructor
	 * @param form_el - our form that should be empowered
	 * @param options - tFormer options
	 * @returns {tFormer}
	 */
	var tFormer = function ( form_el, options ){
		if ( !(this instanceof tFormer) ) {
			return new tFormer( form_el, options );
		}

		var self = this;
		// our main form DOM element
		self.form = (function ( form_el ){
			form_el = typeof(form_el) === 'string' ? document.forms[form_el] : form_el;
			return __isForm( form_el ) ? form_el : null;
		})( form_el );

		var my_form = self.form;
		if ( self.form === null ) {
			return null;
		}

		if ( !__getAttr( my_form, EMPOWERED ) ) {
			__setAttr( my_form, EMPOWERED, 1 );
			__setAttr( my_form, 'novalidate', 'novalidate' );
		} else {
			var cached = (function (){
				for ( var i = 0, c_l = self.cache.length; i < c_l; i++ ) {
					if ( self.cache[i].form == my_form ) {
						return self.cache[i];
					}
				}
				return null;
			})();
			if ( cached ) {
				var initialized = cached.inited;
				cached.set( options );
				return cached;
			}
		}
		self.config = (self.config || __clone( defaults ));
		self.set( options );

		self.init();
		self.cache.push( self );
		return self;
	};
	var tf_proto = tFormer.prototype;
	tf_proto.cache = [];


	tf_proto.init = function (){
		var self = this;
		if ( self.inited ) {
			return self;
		}

		self.fields = {};
		self.buttons = {};

		self.inited = true;

		self.locked = 0;
		self.holded = 0;
		self.invalid = 0;
		self.valid = true;

		self.fields = {};
		self.buttons = {};

		// XHR stuff
		self.xhr = {};
		self.xhrTimeout = {};

		var sb = self.get( 'submitButton' );
		if ( sb ) {
			self.buttons['submit'] = new tButton( self, sb );
		}

		for ( var i = 0, f_l = self.form.length; i < f_l; i++ ) {
			var el = self.form[i],
				type = el.type,
				name = type !== 'button' ? __getAttr( el, 'name' ) : __data( el, 'check' );

			if ( __inArray( FIELD_TYPES, type ) !== -1 && name ) {
				self.fields[name] = new tField( self, el );
			}

			if ( __inArray( BUTTON_TYPES, type ) !== -1 ) {
				name = (type == 'submit') ? type : name;
				if ( name && !(name == 'submit' && self.button[name]) ) {
					self.buttons[name] = new tButton( self, el );
				}
			}
		}

		self.form.onsubmit = (function ( self ){
			return function ( event ){
				event = event || window.event;

				var sb = self.button( 'submit' ),
					sb_control = self.get( 'submitButtonControl' ),
					s_func = typeof self.get( 'submit' ) == 'function',
					processing = sb.get( 'processingClass' ),
					prevent = self.valid && s_func;

				// disable double submit
				if ( (processing && sb.hasClass( processing )) || self.locked ) {
					__prevent( event );
					return false;
				}

				if ( prevent ) {
					__prevent( event );
				}
				if ( self.valid ) {
					if ( sb_control ) {
						sb.processing( true );
					}
					if ( s_func ) {
						self.execute( self.form, 'submit', [event, self] );
					}
				}
				if ( prevent ) {
					return false;
				}

				try {
					if ( !self.valid && !self.validate( { no_timeout: true } ) ) {
						__prevent( event );
						sb.processing( false );
						return false;
					}

					if ( s_func ) {
						__prevent( event );
						self.execute( self.form, 'submit', [event, self] );
						return false;
					}
					self.form.submit();
					return true;

				} catch ( e ) {
				}
			};
		})( self );


		self.validate( {
			highlight : false,
			fire_event: false,

			silence: true
		} );
		return self.submitControl();
	};


	tf_proto.destroy = function (){
		var self = this;
		for ( var name in self.fields ) {
			self.fields[name].destroy();
		}
		for ( var name in this.buttons ) {
			self.buttons[name].destroy();
		}
		self.inited = false;
		return self;
	};

	//	function for dropping options
	tf_proto.drop = function (){
		var self = this,
			fields = self.fields,
			buttons = self.buttons;
		self.destroy();
		self.set( __clone( defaults ) );
		for ( var name in fields ) {
			fields[name].drop();
		}
		for ( var name in buttons ) {
			buttons[name].drop();
		}
		self.locked = 0;
		return self.init();
	};

	tf_proto.validate = function ( options ){
		var self = this,
			fields = self.fields,
			errors = 0;

		for ( var key in fields ) {
			errors += (fields[key].validate( options || {} )) ? 0 : 1;
		}
		self.invalid = errors;
		self.valid = errors === 0;
		return errors === 0;
	};


	tf_proto.toObject = function (){
		var self = this,
			fields = self.form,
			obj = {};

		for ( var i = 0, f_l = fields.length; i < f_l; i++ ) {
			var el = fields[i],
				name = __getAttr( el, 'name' );
			if ( el.type == 'checkbox' ) {
				obj[name] = el.checked;
			} else if ( el.type == 'radio' ) {
				if ( !obj[name] ) {
					obj[name] = '';
				}
				if ( el.checked ) {
					obj[name] = el.value;
				}
			} else if (el.type !== 'submit' && el.type !== 'button'){
				obj[name] = el.value;
			}
		}
		return obj;
	};

	tf_proto.get = function ( option ){
		return this.config[option];
	};

	tf_proto.set = function ( options ){
		var self = this,
			is_inited = self.inited;
		if ( is_inited ) {
			self.destroy();
		}
		self.config = __extend( self.config, options );
		if ( is_inited ) {
			self.init();
		}
		return self;
	};

	/**
	 * Get field object to work with
	 * @param {string} name - field name
	 * @returns {*} - field Object
	 */
	tf_proto.field = function ( name ){
		return this.fields[name];
	};

	/**
	 * Get button object to work with
	 * @param {string} name - button name
	 * @returns {*} - button Object
	 */
	tf_proto.button = function ( name ){
		return this.buttons[name];
	};

	/**
	 * Rewrite default form submit function with current one
	 * (default HTML form submit function will be prevented)
	 * @param {function} func - function that should be executed on form submit
	 * @returns {*}
	 */
	tf_proto.submit = function ( func ){
		var self = this;
		if ( !self.config ) {
			return self;
		}
		if ( typeof func == 'function' ) {
			self.config.submit = func;
		}
		return self;
	};

	/**
	 * Form Submit button control function
	 * (enabling/disabling while validating)
	 * @param {!boolean} valid - is current form valid or not?
	 * @returns {*}
	 */
	tf_proto.submitControl = function ( valid ){
		var self = this,
			sb = self.button( 'submit' ),
			sb_control = self.get( 'submitButtonControl' );

		self.valid = (self.invalid === 0 && self.holded === 0 && self.locked === 0);
		valid = (valid === false || valid === true) ? valid : self.valid;

		if ( sb && sb_control ) {
			sb[(valid) ? 'enable' : 'disable']();
		}
		return self;
	};
	/**
	 * Submit button disable
	 * @returns {*}
	 */
	tf_proto.submitDisable = function (){
		return this.submitControl( false );
	};
	/**
	 * Submit button enable
	 * @returns {*}
	 */
	tf_proto.submitEnable = function (){
		return this.submitControl( true );
	};

	/**
	 * Submit button processing control
	 * @returns {*}
	 */
	tf_proto.processing = function ( action ){
		var self = this,
			sb = self.button( 'submit' );
		if ( sb ) {
			sb.processing( action );
		}
		return self;
	};

	/**
	 * Lock form
	 * @returns {*}
	 */
	tf_proto.lock = function ( num ){
		var self = this;
		self.locked += num || 1;
		return self.submitControl( false );
	};

	/**
	 * Unlock form
	 * @returns {*}
	 */
	tf_proto.unlock = function ( num ){
		var self = this;
		self.locked -= num || 1;
		return self.submitControl();
	};

	/**
	 * Execute function
	 * @param context
	 * @param func
	 * @param params
	 * @returns {*}
	 */
	tf_proto.execute = function ( context, func, params ){
		var self = this;
		if ( typeof func == 'string' ) {
			func = self.get( func );
		}
		if ( typeof func == 'function' ) {
			return func.apply( context, (params || []) );
		}
		return null;
	};

	window.tFormer = tFormer;


	/**
	 * Form element constructor
	 * @returns {*}
	 * @constructor
	 */
	var Element = function (){
	};
	var El_p = Element.prototype;
	El_p.destroy = function (){
		var self = this,
			el = this.el,
			events = self.events;

		for ( var i = 0, e_l = events.length; i < e_l; i++ ) {
			self.off( events[0][0], events[0][1] );
		}

		self.removeClass( self.get( 'errorClass' ) );
		self.removeClass( self.get( 'desabledClass' ) );
		self.removeClass( self.get( 'processignClass' ) );

		__data( el, 'holded', null );
		__data( el, 'error', null );
		// remove hold attributes

		if ( self.timer ) {
			clearTimeout( self.timer );
		}
		if ( self.xhr ) {
			self.xhr.abort();
		}
		if ( self.xhrTimeout ) {
			clearTimeout( self.xhrTimeout );
		}

		if ( !self.valid ) {
			self.parent.invalid = self.parent.invalid !== 0 ? self.parent.invalid - 1 : 0;
		}

		self.parent.submitControl();

		self.inited = false;
		return self;
	};

	El_p.drop = function (){
		return this.set( __clone( defaults ) );
	};

	El_p.set = function ( options ){
		var self = this,
			name = __getAttr( self.el, 'name' ),
			_set = function ( key, value ){
				self.config[key] = value;
				if ( !self.parent.config.fields[name] ) {
					self.parent.config.fields[name] = __clone( defaults );
				}
				self.parent.config.fields[name][key] = value;
			},
			is_inited = self.inited;

		if ( is_inited ) {
			self.destroy();
		}
		for ( var key in options ) {
			if ( ~__inArray( FIELD_OPTIONS, key ) ) {
				_set( key, options[key] );
			}
		}
		if ( is_inited ) {
			self.init();
		}
		return self;
	};

	El_p.get = function ( option ){
		return this.config[option];
	};

	/**
	 * subscribe this.el to some event
	 * @param {string} evnt - event name
	 * @param {function} func - function that should be executed on event
	 * @param {object} el - element to attach event
	 * @returns {*}
	 */
	El_p.on = function ( evnt, func, el ){
		var self = this,
			el = el || self.el,
			events = evnt.split( ' ' );

		for ( var i = 0, e_l = events.length; i < e_l; i++ ) {
			if ( el.addEventListener ) { // W3C DOM
				el.addEventListener( events[i], func, false );
			} else if ( el.attachEvent ) { // IE DOM
				el.attachEvent( "on" + events[i], func );
			} else { // No much to do
				el[events[i]] = func;
			}
			self.events.push( [events[i], func] );
		}
		return self;
	};

	/**
	 * unsubscribe this.el (Button || Field) from some event
	 * @param {string} evnt - event name
	 * @param {function} func - function that should be executed on event
	 * @returns {*}
	 */
	El_p.off = function ( evnt, func ){
		var self = this,
			el = self.el,
			events = self.events;

		evnt = evnt.split( ' ' );
		if ( !func ) {
			for ( var i = 0, e_l = events.length; i < e_l; i++ ) {
				if ( __inArray( evnt, events[i][0] ) !== -1 ) {
					events.splice( i, 1 );
				}
			}
			return self;
		}

		if ( el.removeEventListener ) { // W3C DOM
			el.removeEventListener( evnt, func, false );
		} else if ( el.detachEvent ) { // IE DOM
			el.detachEvent( "on" + evnt, func );
		} else { // No much to do
			el[evnt] = null;
		}

		for ( var i = 0, e_l = events.length; i < e_l; i++ ) {
			if ( __inArray( evnt, events[i][0] ) !== -1 && events[i][1] == func ) {
				events.splice( i, 1 );
				return self;
			}
		}
		return self;
	};

	/**
	 * fire some event for this.field
	 * @param {string} evnt - event name
	 * @returns {*}
	 */
	El_p.trigger = function ( evnt ){
		var self = this,
			el = self.el,
			evt;

		if ( self.silence ) {
			return;
		}

		try {// every browser except IE8 and below works here
			evt = document.createEvent( "HTMLEvents" );
			evt.initEvent( evnt, true, true );
			return !el.dispatchEvent( evt );
		} catch ( err ) {
			try {
				return el.fireEvent( 'on' + evnt );
			} catch ( error ) {
			}
		}
		return self;
	};


	El_p.addClass = function ( new_class ){
		var self = this,
			el = self.el,
			class_names = el.className.split( ' ' ) || [];

		if ( __inArray( class_names, new_class ) === -1 ) {
			class_names.push( new_class );
			class_names = __clear( class_names );
			el.className = (class_names.length > 0) ? class_names.join( ' ' ) : '';
		}
		return self;
	};

	El_p.removeClass = function ( old_class ){
		var self = this,
			el = self.el;

		if ( self.hasClass( old_class ) ) {
			var re = new RegExp( '(\\s|^)' + old_class + '(\\s|$)' );
			el.className = el.className.replace( re, ' ' );
		}
		return self;
	}

	El_p.hasClass = function ( name ){
		return !!((~(' ' + this.el.className + ' ').indexOf( ' ' + name + ' ' )));
	};

	El_p.data = function ( attr, value ){
		var self = this,
			el = self.el,
			result = __data( el, attr, value );

		if ( value === undefined ) {
			return result;
		}
		return self;
	};

	El_p.attr = function ( attr, value ){
		var self = this,
			el = self.el;
		switch ( value ) {
			case null:
				__delAttr( el, attr );
				break;
			case undefined:
				return __getAttr( el, attr );
				break;
			default:
				__setAttr( el, attr, value );
				break;
		}
	};

	El_p.processing = function ( action ){
		var self = this,
			processingClass = self.get( 'processingClass' ),
			is_processing = self.hasClass( processingClass );

		if ( action === false || (action === null && is_processing) ) {
			self.removeClass( processingClass );
		} else if ( action === true || (action === null && is_processing) ) {
			self.addClass( processingClass );
		}
		return this;
	};


	/** extent subclass with superclass prototype */
	var __extend_proto = function ( Child, Parent ){
		var F = function (){
		}
		F.prototype = Parent.prototype
		Child.prototype = new F()
		Child.prototype.constructor = Child
		Child.superclass = Parent.prototype
	};


	var tField = function ( parent, el ){
		var self = this,
			type = el.type,
			name, rules,
			attr_required, attr_min, attr_max,
			rules2add = [],
			config;

		self.parent = parent;
		self.el = el;
		self.config = {};

		self.events = [];
		name = self.attr( 'name' );
		attr_required = self.attr( 'required' ) !== null;
		attr_min = self.attr( 'min' );
		attr_max = self.attr( 'max' );

		config = parent.config.fields ? parent.config.fields[name] : {};
		if ( typeof config == 'string' ) {
			config = {
				rules: config
			};
		}
		self.set( __extend( __clone( parent.config ), __clone( config ) ) );
		self.config.rules = self.config.rules || self.data( 'rules' );

		if ( attr_required ) {
			rules2add.push( '*' );
		}

		if ( type == 'email' ) {
			rules2add.push( '@' );
		}

		if ( type == 'url' ) {
			rules2add.push( 'url' );
		}

		if ( type == 'number' ) {
			rules2add.push( 'num' )

			if ( attr_min !== null ) {
				rules2add.push( '>' + attr_min );
			}
			if ( attr_max !== null ) {
				rules2add.push( '<' + attr_max );
			}
		}


		if ( rules2add.length > 0 ) {
			self.config.rules = _v_( '' ).rules( self.config.rules || self.data( 'rules' ) ).addRule( rules2add.join( ' ' ) ).rule;
		}

		self.value = el.value;

		// validate after init
		self.validationStart = 'v_start';
		self.validationSuccess = 'v_success';
		self.validationError = 'v_error';

		self.highlight = true;
		self.fire_event = true;
		self.silence = false;

		return self.init();
	};
	__extend_proto( tField, Element );
	var tField_p = tField.prototype;

	tField_p.init = function (){
		var self = this,
			field = self.el,
			value = field.value,
			type = self.attr( 'type' ),
			is_checkbox = type == 'checkbox';

		if ( self.inited ) {
			return self;
		}

		self.events = [];

		self.valid = true;
		self.holded = false;

		self.value = value;

		// adding validate event to the field;
		var validate_event = self.get( 'validateEvent' );

		if ( ~__inArray( CHANGE_ALSO, type ) && validate_event.indexOf( 'change' ) === -1 ) {
			validate_event = validate_event.split( ' ' );
			validate_event.push( 'change' );
			validate_event = validate_event.join( ' ' );
		}
		if ( ~__inArray( HAS_CHANGE_EVENT, type ) ) {
			validate_event = 'change';
		}

		self.set( {
			validateEvent: validate_event
		} );

		self.on( validate_event, function (){
			if ( !self.get( 'rules' ) ) {
				return;
			}
			if ( self.value != self.el.value || is_checkbox ) {
				self.value = self.el.value;

				// clear field before validation
				self.removeClass( self.get( 'errorClass' ) );
				self.removeClass( self.get( 'processingClass' ) );

				// disable submit button before validation
				self.parent.invalid += (self.valid) ? 1 : 0;
				self.valid = false;
				self.removeClass( self.get( 'errorClass' ) );
				self.parent.submitControl();

				var timeout = self.get( 'timeout' );
				if ( self.get( 'timeout' ) > 0 ) {
					if ( self.timer ) {
						clearTimeout( self.timer );
					}
					self.timer = setTimeout( function (){
						self.validate();
					}, timeout );
				} else {
					self.validate();
				}
			}
		} );


		if ( self.hasRules( '=#' ) ) {
			var self_v_ = _v_().rules( self.config.rules ),
				depended_id = self_v_.parsedRules['=#'],
				el = document.getElementById( depended_id );

			if ( el ) {
				self.on( 'input keyup', function ( e ){
					self.validate( {
						highlight: !!self.value
					} );
				}, el )
			}
		}

		// blur validation without timeout
		if ( !~validate_event.indexOf( 'blur' ) && validate_event !== 'change' ) {
			self.on( 'blur', function (){
				if ( !self.get( 'rules' ) ) {
					return;
				}
				if ( self.timer ) {
					clearTimeout( self.timer );
				}
				if ( !(self.valid && self.hasRules( 'request' ) ) ) {
					self.validate( {
						no_timeout: true
					} );
				}
			} );
		}

		self.validate( { silence: true } );

		self.inited = true;
		return self;
	};
	tField_p.setRules = function ( rules, options ){
		var self = this;
		self.set( {
			rules: rules
		}, options );
		self.validate( options );
		return self;
	};

	tField_p.hasRules = function ( rules ){
		return _v_().rules( this.get( 'rules' ) ).hasRule( rules );
	};

	tField_p.addRules = function ( rules, options ){
		var self = this;
		return self.setRules( _v_().rules( self.get( 'rules' ) ).addRule( rules ).rule, options );
	};

	tField_p.delRule = function ( rules, options ){
		var self = this;
		return self.setRules( _v_().rules( self.get( 'rules' ) ).delRule( rules ).rule, options );
	};

	/**
	 * Highlight field with errorClass
	 * @param valid
	 * @returns {*}
	 */
	tField_p.error = function ( valid ){
		var self = this;
		self.valid = (!valid) ? true : false;

		if ( !self.highlight && !self.valid ) {
			return this;
		}

		var field = self.el,
			errorClass = self.get( 'errorClass' );

		if ( self.valid ) {
			self.removeClass( errorClass );
			self.data( 'error', null );
		} else {
			self.addClass( errorClass );
			self.data( 'error', '1' );
		}
		return self;
	};

	/**
	 * Hold field for a while
	 * @param {!boolean} hold
	 * @returns {*}
	 */
	tField_p.hold = function ( hold ){
		var self = this,
			is_holded = self.data( 'holded' );

		if ( hold === undefined ) {
			self.holded = !self.holded;
		} else {
			self.holded = (hold === true) ? true : false
		}
		self.data( 'holded', (self.holded ? 1 : null) );
		if ( !is_holded && self.holded === true ) {
			self.parent.holded++;
		} else if ( is_holded && self.holded === false ) {
			self.parent.holded--;
		}
		self.parent.submitControl();
		return self;
	};

	/**
	 * Here is the main field validation process
	 * @param {object} options
	 * @returns {boolean}
	 */
	tField_p.validate = function ( options ){
		var self = this,
			field = self.el,
			type = self.attr( 'type' ),
			result = true,
			own = self.get( 'own' ),
			request = self.get( 'request' ),
			rules = self.get( 'rules' ),
			_v_check = _v_( self.el.value || '' ).rules( rules ),
			is_checkbox = type == 'checkbox',
			is_required = _v_check.hasRule( '*' );

		if ( !rules ) {
			return result;
		}

		options = options || {};
		self.silence = (options.silence === true) ? true : false;

		self.highlight = (options.highlight === false || options.silence === true) ? false : true;
		self.fire_event = (options.fire_event === false || options.silence === true) ? false : true;

		if ( !self.silence ) {
			self.execute( 'before' );
			self.trigger( self.get( 'eventBefore' ) );
			self.trigger( self.validationStart );
		}

		if ( typeof own == 'function' ) {
			result = own.call( self.el );
		} else {
			if ( is_checkbox ) {
				var is_checked = field.checked;
				if ( !is_checked && is_required ) {
					result = false;
				}
			} else {
				// check request validation
				if ( is_required || self.el.value.length > 0 ) {
					result = _v_check.validate();
				}

				if ( request && result ) {
					self.requestValidate( options );
					self.highlight = true;
					return null;
				}
			}
		}

		if ( result ) {
			self.__validationSuccess();
		} else {
			self.__validationError();
		}

		self.highlight = true;
		self.fire_event = true;
		self.silence = false;
		return result;
	};

	tField_p.__validationStart = function (){

	};

	tField_p.__validationError = function (){
		var self = this;
		self.trigger( self.get( 'eventError' ) );
		self.parent.invalid += (self.valid) ? 1 : 0;
		self.parent.submitControl();
		self.error( true );
		self.execute( 'onerror' );
	};
	tField_p.__validationSuccess = function (){
		var self = this;
		self.trigger( self.get( 'eventValid' ) );
		self.parent.invalid -= (!self.valid) ? 1 : 0;
		self.parent.submitControl();
		self.error( false );
		self.execute( 'onvalid' );
	};


	tField_p.requestValidate = function ( options ){

		var self = this,
			name = self.attr( 'name' ),
			value = self.el.value,
			request = self.get( 'request' ),
			check_btn = self.parent.button( __getAttr( self.el, 'name' ) ),
			method = request.method.toLowerCase() == 'post' ? 'POST' : 'GET',
			data = request.data || {},
			success = request.success,
			url = (function (){
				var url = request.url || window.location.href;
				if ( method == 'GET' ) {
					url += (~url.indexOf( '?' )) ? '&' : '?';
					url += name + '=' + value;
				} else {
					data[name] = value;
				}
				return url;
			})(),

			timeout = options.no_timeout ? 0 : (request.timeout || 0),

			readyStateChange = function (){
				var xhr = self.xhr;

				if ( xhr.readyState == 1 ) {
					self.execute( request.start, [xhr] );
				}

				if ( xhr.readyState == 4 ) {
					// TODO: handle other errors (maybe with switch);
					if ( xhr.status == 200 ) {
						var result = (self.execute( request.end, [xhr.response] ) === true) ? true : false;
						self['__validation' + (result ? 'Success' : 'Error')]();
					}
				}
				if ( xhr.readyState == 4 || xhr.readystate == 0 ) {
					self.processing( false ).hold( false );
					if ( check_btn ) {
						check_btn.processing( false );
					}
				}
			},

			makeRequest = function (){
				self.processing( true ).hold( true );
				if ( check_btn ) {
					check_btn.processing( true );
				}
				var xhr = HTTP.newRequest();
				self.xhr = xhr;
				xhr.onreadystatechange = readyStateChange;
				xhr.open( method, url, true );
				xhr.setRequestHeader( "Accept-Language", "en" );
				if ( method == 'POST' ) {
					xhr.setRequestHeader( "Content-type", "application/x-www-form-urlencoded; charset=UTF-8" );
					xhr.send( __serialize( data ) );
				} else {
					xhr.send( null );
				}
			};

		if ( self.xhr && (self.xhr.readyState !== 0 || self.xhr.readyState !== 4) ) {
			self.xhr.abort();
			self.processing( false ).hold( false );
			if ( check_btn ) {
				check_btn.processing( false );
			}
		}

		if ( self.xhrTimeout ) {
			clearTimeout( self.xhrTimeout );
		}
		self.hold( false );

		if ( timeout > 0 && options.no_timeout !== true ) {
			self.xhrTimeout = setTimeout( function (){
				makeRequest();
			}, timeout );
		} else {
			makeRequest();
		}
	};

	tField_p.execute = function ( func, params ){
		var self = this;
		if ( self.silence ) {
			return;
		}

		if ( typeof func == 'string' ) {
			func = self.get( func );
		}
		return self.parent.execute( self.el, func, params );
	};


	/*
	 * Test tButton created by Element constructor
	 */
	var tButton = function ( parent, el ){
		var self = this,
			type = self.attr( 'type' ),
			name;

		self.parent = parent;
		self.el = el;
		self.config = {};

		self.events = [];

		name = type === 'submit' ? type : self.data( 'check' );
		self.name = name;
		self.set( __extend( __clone( parent.config ), __clone( (parent.config.buttons ? parent.config.buttons[name] : {}) ) ) );

		return self.init();
	};
	__extend_proto( tButton, Element );
	var tButton_p = tButton.prototype;

	tButton_p.init = function (){
		var self = this,
			el = self.el,
			parent = self.parent;

		if ( self.inited ) {
			self.destroy();
		}
		if ( el.type == 'submit' || el == parent.get( 'submitButton' ) ) {
			self.on( 'click', function ( e ){
				__prevent( e );
				parent.form.onsubmit( e );
				return false;
			} );
		} else {
			self.on( 'click', function (){
				var field = parent.field( self.data( 'check' ) );
				if ( field ) {
					field.validate( {no_timeout: true} );
				}
			} );
		}
		this.inited = true;
		return this;
	};

	tButton_p.disable = function (){
		var self = this;
		self.addClass( self.get( 'disabledClass' ) );
		return self;
	};

	tButton_p.enable = function (){
		var self = this;
		self.removeClass( self.get( 'disabledClass' ) );
		return self;
	};


	/*
	 * Helpers
	 * ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
	 */
	/**
	 * Object extend
	 * @param object
	 * @param new_obj
	 * @returns {object}
	 */
	var __extend = function ( object, new_obj ){
		for ( var key in new_obj ) {
			if ( new_obj.hasOwnProperty( key ) ) {
				object[key] = new_obj[key];
			}
		}
		return object;
	};

	/**
	 * Method for preventing default events
	 * @param e
	 * @private
	 */
	var __prevent = function ( e ){
		if ( e.preventDefault ) {
			e.preventDefault();
		} else {
			event.returnValue = false;
		}
	};

	/**
	 * Object clone
	 * @returns {*|array|string}
	 */
	var __clone = function ( obj ){
		return __isArray( obj ) ? obj.slice() : __extend( {}, obj );
	};


	/**
	 * is array function
	 * @returns {boolean}
	 */
	var __isObject = function ( obj ){
		return toString.call( obj ) == '[object Object]';
	};


	var __isForm = function ( obj ){
		return obj && obj.nodeName === 'FORM';
	};

	/**
	 * is array function
	 * @returns {boolean}
	 */
	var __isArray = function ( obj ){
		return Object.prototype.toString.call( obj ) == '[object Array]';
	};


	/**
	 * detects is defined array has some value
	 * @param array
	 * @param value
	 * @returns {number}
	 * @private
	 */
	var __inArray = function ( array, value ){
		var index = -1,
			length = array ? array.length : 0;
		while ( ++index < length ) {
			if ( array[index] === value ) {
				return index;
			}
		}
		return -1;
	};

	var __clear = function ( arr ){
		if ( __isArray( arr ) ) {
			var new_arr = [];
			for ( var i = 0, a_l = arr.length; i < a_l; i++ ) {
				if ( arr[i] !== '' ) {
					new_arr.push( arr[i] );
				}
			}
			return new_arr;
		}
	};


	/**
	 * Work with data-attributes
	 *
	 * @param {object} element - element
	 * @param {string} attr - data-attribute
	 * @param {!string|number} value - new attribute value. [null - delete attr, undefined - return attr value, defined - set new value]
	 * @returns {*}
	 */
	var __data = function ( element, attr, value ){
		switch ( value ) {
			case null:
				__delAttr( element, 'data-' + attr );
				break;
			case undefined:
				return __getAttr( element, 'data-' + attr );
				break;
			default:
				__setAttr( element, 'data-' + attr, value );
				break;
		}
	};

	var __getAttr = function ( el, attr ){
		if ( !el ) {
			return null;
		}
		return el.getAttribute( attr );
	};
	var __setAttr = function ( el, attr, value ){
		if ( !el ) {
			return null;
		}
		el.setAttribute( attr, value );
	};
	var __delAttr = function ( el, attr ){
		if ( !el ) {
			return null;
		}
		el.removeAttribute( attr );
	};


	// AJAX Request functionality
	var HTTP = {};
	HTTP._factories = [
		function (){
			return new XMLHttpRequest();
		},
		function (){
			return new ActiveXObject( "Msxml2.XMLHTTP" );
		},
		function (){
			return new ActiveXObject( "Microsoft.XMLHTTP" );
		}
	];
	HTTP._factory = null;
	HTTP.newRequest = function (){
		if ( HTTP._factory !== null ) {
			return HTTP._factory();
		}
		for ( var i = 0; i < HTTP._factories.length; i++ ) {
			try {
				var factory = HTTP._factories[i];
				var request = factory();
				if ( request !== null ) {
					HTTP._factory = factory;
					return request;
				}
			} catch ( e ) {
				continue;
			}
		}
		HTTP._factory = function (){
			throw new Error( 'Object XMLHttpRequest not supported' );
		};
		HTTP._factory();
	};


	/**
	 * Serrialize data for request
	 * @param {object} data - object to serialize
	 * @returns {string}
	 */
	var __serialize = function ( data ){
		var pairs = [];
		var regexp = /%20/g;
		for ( var name in data ) {
			var pair = encodeURIComponent( name ).replace( regexp, '+' ) + '=';
			pair += encodeURIComponent( data[name].toString() ).replace( regexp, '+' );
			pairs.push( pair );
		}
		return pairs.join( '&' );
	};

})( window, document );
/**
 * _v_.js - validator
 * http://github.com/TjRus/_v_.js
 * (c) 2013 Vasiliy Zubach (aka TjRus) - http://tjrus.com/
 * _v_ may be freely distributed under the MIT license.
 */
"use strict";

(function ( window, document, undefined ){

	/**
	 * Validator constructor
	 *
	 * @constructor
	 * @param {!string} value
	 * @returns {*}
	 * @private
	 */
	var _v_ = function ( value ){
		if ( !(this instanceof _v_) ) {
			return new _v_( value );
		}
		this.value = value || '';
		this.separator = ' ';
		this.rule = '';

		this.parsedRules = [];

		return this;
	};
	var _v_proto = _v_.prototype;

	/**
	 * sets rules separator
	 * @param separator
	 * @returns {*}
	 */
	_v_proto.separate = function ( separator ){
		this.separator = separator;
		this.rules( this.rule ); // pars rules again
		return this;
	};

	/**
	 * set rules to validator
	 * @param rules
	 * @returns {*}
	 */
	_v_proto.rules = function ( rules ){
		this.rule = rules || '';
		this.parseRules();
		return this;
	};

	/**
	 * add rules to existed rules str
	 * @param rule
	 * @returns {*}
	 */
	_v_proto.addRule = function ( rule ){
		var parsed = this.parsedRules;
		var rule_v_ = _v_().rules( rule ).parsedRules;

		for ( var key in rule_v_ ) {
			var rule = rule_v_[key];
			if ( !rule ) {
				parsed[key] = rule;
				continue;
			}
			// has params and is in defined rules
			if ( rule && parsed.hasOwnProperty( key ) ) {
				// params is array
				parsed[key] = __toArray( parsed[key] );
				rule = __toArray( rule );
				for ( var i = 0, r_v_l = rule.length; i < r_v_l; i++ ) {
					if ( __inArray( parsed[key], rule[i] ) !== -1 ) {
						continue;
					}
					parsed[key].push( rule[i] );
				}
			} else {
				parsed[key] = rule;
			}
		}

		this.rule = __rulesStr( this.parsedRules, this.separator );
		return this;
	};

	/**
	 * Delete rule from validator rules
	 * @param rule
	 * @returns {*}
	 */
	_v_proto.delRule = function ( rule ){
		var parsed = this.parsedRules;
		var rule_v_ = _v_().rules( rule ).parsedRules;
		for ( var key in rule_v_ ) {
			var rules = rule_v_[key];
			if (!parsed.hasOwnProperty(key)) {
				continue;
			}
			if ( rules === undefined) {
				delete parsed[key];
				continue;
			}

			parsed[key] = __toArray( parsed[key] );
			rules = __toArray( rules );
			for ( var i = 0, r_l = rules.length; i < r_l; i++ ) {
				var index = __inArray( parsed[key], rules[i] );
				if ( ~index ) {
					parsed[key].splice( index, 1 );
				}
			}
			if ( parsed[key].length === 0 ) {
				delete parsed[key];
			} else if ( parsed[key].length === 1 ) {
				parsed[key] = parsed[key][0];
			}
		}
		this.rule = __rulesStr( this.parsedRules, this.separator );
		return this;
	};

	/**
	 * check has validator such rule or not
	 * @param rules
	 * @returns {boolean}
	 */
	_v_proto.hasRule = function ( rules ){
		var rule_v_ = _v_().rules( rules ).parsedRules;
		var parsed = this.parsedRules;
		for ( var key in rule_v_ ) {
			var rule = rule_v_[key];
			if ( !rule ) {
				if ( !parsed.hasOwnProperty( key ) ) {
					return false;
				} else {
					continue;
				}
			}
			parsed[key] = __toArray( parsed[key] );
			rule = __toArray( rule );
			for ( var i = 0, r_l = rule.length; i < r_l; i++ ) {
				if ( __inArray( parsed[key], rule[i] ) === -1 ) {
					return false;
				}
			}
		}
		return true;
	};


	/**
	 * parse validator rules and return object with rule keys and their values
	 * @returns {{}}
	 */
	_v_proto.parseRules = function (){
		var rules = this.rule.split( this.separator );
		var parsed = {};
		var keys = this.keys;

		for ( var i = 0, rules_length = rules.length; i < rules_length; i++ ) {
			var option = rules[i], func, rule, params = undefined;
			if ( keys[ option ] ) {
				func = keys[ option ];
				rule = option;
			} else {
				var keys_order = this.keys_order;
				for ( var j = 0, koLength = keys_order.length; j < koLength; j++ ) {
					var key = keys_order[j];
					if ( option.indexOf( key ) === 0 ) {
						rule = key;
						params = option.replace( key, '' );
						var paramArray = (/^\[(.+)\]$/).exec( params );
						if ( paramArray ) params = paramArray[1].split( ',' ); // TODO: params separator
						func = this.keys[rule];
						break;
					}
				}
			}
			if ( func ) {
				parsed[rule] = params;
			}
		}
		this.parsedRules = parsed;
		this.rule = __rulesStr( parsed, this.separator );
		return parsed;
	};

	/**
	 * main validate function.
	 * @param rules
	 * @returns {boolean}
	 */
	_v_proto.validate = function ( rules ){
		if ( rules ) {
			this.rules( rules );
		}
		var parsed = this.parsedRules;
		for ( var rule in parsed ) {
			try {
			if ( !this.keys[rule].call( this, parsed[rule] ) ) {
				return false;
			}
		} catch (e) {
			return false;
		}
		}
		return true;
	};


	/**
	 * method for extending _v_ with new rules and validate functions
	 * @param rule
	 * @param func
	 */
	_v_proto.extend = function ( rule, func ){
		_v_proto.keys[rule] = func
		_v_proto.keys_order.push( rule );

		_v_proto.keys_order = this.keys_order.sort( function ( a, b ){
			return b.length - a.length;
		} );
		return this;
	};

	_v_proto.keys = {}; // object with rules
	_v_proto.keys_order = []; // array with ordered rules

	window._v_ = _v_;


	/**
	 * Rules extends
	 * ---------- ---------- ---------- ---------- ----------
	 */
	var rules = {

		// required
		'*'   : function (){
			return this.value.length !== 0;
		},

		// alpha
		'a'   : function (){
			return (/^[a-z]+$/i).test( this.value );
		},

		// alpha numeric
		'a1'  : function (){
			return (/^[a-z0-9]+$/i).test( this.value );
		},

		// alpha dash
		'a_'  : function (){
			return (/^[a-z_-]+$/i).test( this.value );
		},

		// alpha numeric dash
		'a1_' : function (){
			return (/^[a-z0-9_-]+$/i).test( this.value );
		},

		// email
		'@'   : function (){
			var mail_regexp = /^((([a-z]|\d|[!#\$%&'\*\+\-\/=\?\^_`{\|}~]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])+(\.([a-z]|\d|[!#\$%&'\*\+\-\/=\?\^_`{\|}~]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])+)*)|((\x22)((((\x20|\x09)*(\x0d\x0a))?(\x20|\x09)+)?(([\x01-\x08\x0b\x0c\x0e-\x1f\x7f]|\x21|[\x23-\x5b]|[\x5d-\x7e]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(\\([\x01-\x09\x0b\x0c\x0d-\x7f]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]))))*(((\x20|\x09)*(\x0d\x0a))?(\x20|\x09)+)?(\x22)))@((([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])*([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])))\.)+(([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])*([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])))$/i;
			return mail_regexp.test( this.value );
		},

		// emails
		'@s'  : function (){
			var emails = this.value.split( ',' );
			for ( var i = 0; i < emails.length; i++ ) {
				if ( !_v_( emails[i] ).validate( '@' ) ) {
					return false;
				}
			}
			return true;
		},

		// ip address
		'ip'  : function (){
			return (/^((25[0-5]|2[0-4][0-9]|1[0-9]{2}|[0-9]{1,2})\.){3}(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[0-9]{1,2})$/i).test( this.value );
		},

		// base65 string
		'b64' : function (){
			return (/^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=|[A-Za-z0-9+\/]{4})$/).test( this.value );
		},

		// URL
		'url' : function (){
			return (/^(https?|s?ftp):\/\/(((([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(%[\da-f]{2})|[!\$&'\(\)\*\+,;=]|:)*@)?(((\d|[1-9]\d|1\d\d|2[0-4]\d|25[0-5])\.(\d|[1-9]\d|1\d\d|2[0-4]\d|25[0-5])\.(\d|[1-9]\d|1\d\d|2[0-4]\d|25[0-5])\.(\d|[1-9]\d|1\d\d|2[0-4]\d|25[0-5]))|((([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])*([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])))\.)+(([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])*([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])))\.?)(:\d*)?)(\/((([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(%[\da-f]{2})|[!\$&'\(\)\*\+,;=]|:|@)+(\/(([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(%[\da-f]{2})|[!\$&'\(\)\*\+,;=]|:|@)*)*)?)?(\?((([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(%[\da-f]{2})|[!\$&'\(\)\*\+,;=]|:|@)|[\uE000-\uF8FF]|\/|\?)*)?(#((([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(%[\da-f]{2})|[!\$&'\(\)\*\+,;=]|:|@)|\/|\?)*)?$/i).test( this.value );
		},

		// integer
		'int' : function (){
			return (/^\-?[0-9]+$/).test( this.value );
		},

		// Numeric
		'num' : function (){
			return (/^[0-9]+$/).test( this.value );
		},

		// Decimal
		'dec' : function (){
			return (/^\-?[0-9]*\.?[0-9]+$/).test( this.value );
		},

		// Natural
		'nat' : function (){
			return (/^[0-9]+$/i).test( this.value );
		},

		// length equals to
		'l='  : function ( length ){
			if ( typeof(length) == 'number' || typeof(length) == 'string' ) {
				return this.value.length == length;
			} else {
				for ( var key in length ) {
					if ( this.value.length == length[key] ) return true;
				}
			}
			return false;
		},

		// length more than
		'l>'  : function ( length ){
			return this.value.length > length;
		},

		// length more or equals to
		'l>=' : function ( length ){
			return this.value.length >= length;
		},

		// length less than
		'l<'  : function ( length ){
			return this.value.length < length;
		},

		// length less or equals to
		'l<=' : function ( length ){
			return this.value.length <= length;
		},

		// length is in range
		'lr=' : function ( range ){
			return (this.value.length >= range[0] && this.value.length <= range[1]);
		},

		// is greater than
		'>'   : function ( value ){
			var test = this.value;
			return (_v_( test ).validate( 'dec' ) && parseFloat( test ) > parseFloat( value ));
		},

		// is greater or equals to
		'>='  : function ( value ){
			var test = this.value;
			return (_v_( test ).validate( 'dec' ) && parseFloat( test ) >= parseFloat( value ));
		},

		// is less than
		'<'   : function ( value ){
			var test = this.value;
			return (_v_( test ).validate( 'dec' ) && parseFloat( test ) < parseFloat( value ));
		},

		// is less or equals to
		'<='  : function ( value ){
			var test = this.value;
			return (_v_( test ).validate( 'dec' ) && parseFloat( test ) <= parseFloat( value ));
		},

		// is in range
		'r='  : function ( value ){
			var test = this.value;
			return (_v_( test ).validate( 'dec' ) && parseFloat( test ) >= parseFloat( value[0] ) && parseFloat( test ) <= parseFloat( value[1] ));
		},

		// regular expression validation
		'reg=': function ( regExpression ){
			var reg = new RegExp( regExpression, 'i' );
			return reg.test( this.value );
		},

		// matches to
		'='   : function ( value ){
			var test = this.value;
			if ( typeof value == 'string' || typeof value == 'number' ) {
				return test == value;
			} else {
				for ( var i = 0, valueLength = value.length; i < valueLength; i++ ) {
					if ( value[i].indexOf( '#' ) === 0 ) {
						var el = __getElById( value[i].replace( '#', '' ) );
						if ( !el ) {
							return false;
						}
						if ( test == el.value ) return true;
					} else {
						if ( test == value[i] ) return true;
					}
				}
			}
			return false;
		},

		// matches to id
		'=#'  : function ( value ){
			var test = this.value;
			if ( typeof value == 'string' || typeof value == 'number' ) {
				value = value.split( ' ' );
				var el = __getElById( value );
				if ( !el ) {
					return false;
				}
				return test == el.value;
			} else {
				for ( var i = 0; i < value.length; i++ ) {
					var el = __getElById( value[i] );
					if ( el && test == el.value ) {
						return true;
					}
				}
			}
			return false;
		},

		// not matches to
		'!='  : function ( value ){
			value = (__isArray( value )) ? '[' + value.join( ',' ) + ']' : value; // TODO: value separator
			return !(_v_( this.value ).validate( '=' + value ));
		},

		// not contain
		'!'   : function ( value ){
			if ( typeof value == 'string' || typeof value == 'number' ) {
				return (this.value).toString().indexOf( value.toString() ) === -1;
			} else {
				for ( var key in value ) {
					if ( ~(this.value).toString().indexOf( value[key].toString() ) ) {
						return false;
					}
				}
			}
			return true;
		},

		// credit card (all cards type)
		'c'   : function ( value ){
			return (/^(?:4[0-9]{12}(?:[0-9]{3})?|5[1-5][0-9]{14}|6(?:011|5[0-9][0-9])[0-9]{12}|3[47][0-9]{13}|3(?:0[0-5]|[68][0-9])[0-9]{11}|(?:2131|1800|35\d{3})\d{11})$/).test( this.value );
		},

		// visa card
		'cv'  : function ( value ){
			return (/^4[0-9]{12}(?:[0-9]{3})?$/).test( this.value );
		},

		// master card
		'cm'  : function ( value ){
			return (/^5[1-5][0-9]{14}$/).test( this.value );
		},

		// american express card
		'ca'  : function ( value ){
			return (/^3[47][0-9]{13}$/).test( this.value );
		},

		// discover card
		'cd'  : function ( value ){
			return (/^6(?:011|5[0-9]{2})[0-9]{12}$/).test( this.value );
		},

		// date format validation
		'D='  : function ( format ){
			return !!(__toDate( this.value, format ));
		}
	};

	// add extends
	for ( var key in rules ) {
		_v_().extend( key, rules[key] );
	}


	/**
	 * Helpers
	 * ---------- ---------- ---------- ---------- ----------
	 */

	// Date functions
	var __dayNames = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];
	var __shortDayNames = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'];
	var __dayChars = ['S', 'M', 'T', 'W', 'T', 'F', 'S'];

	// Full, short and single character names for the months.  Override these to provide multi-language support.
	var __monthNames = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'];
	var __shortMonthNames = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
	var __monthChars = ['J', 'F', 'M', 'A', 'M', 'J', 'J', 'A', 'S', 'O', 'N', 'D'];

	var __daysInMonth = function ( month, year ){
		// If February, check for leap year
		if ( (month == 1) && (((year % 4 === 0) && (year % 100 !== 0)) || (year % 400 === 0)) ) {
			return 29;
		}
		else {
			var days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
			return days[month];
		}
	};

	/**
	 * Attempts to convert a string into a date based on a given format.  Fields will
	 * match either the long or short form, except in the case of the year, where the
	 * string must match either a 2-digit or 4-digit format.  Ranges are checked.  Day
	 * names are expected if they are included in the format string, but are otherwise
	 * ignored.  Use ^ to force the use of a literal character. In other words, to
	 * have the character Y appear instead of the actual year, use ^Y.
	 *
	 * Field        | Full Form           | Short Form
	 * -------------+---------------------+-------------------
	 * Year         | Y (4 digits)        | y (2 digits)
	 * Month        | M (1 or 2 digits)   | m (1 or 2 digits)
	 * Month Name   | N (full name)       | n (abbr)
	 * Day of Month | D (1 or 2 digits)   | d (1 or 2 digits)
	 * Day Name     | W (full name)       | w (abbr)
	 * Hour (1-12)  | H (1 or 2 digits)   | h (1 or 2 digits)
	 * Hour (0-23)  | R (1 or 2 digits)   | r (1 or 2 digits)
	 * Minute       | I (1 or 2 digits)   | i (1 or 2 digits)
	 * Second       | S (1 or 2 digits)   | s (1 or 2 digits)
	 * AM/PM        | A (upper case)      | a (lower case)
	 *
	 * @param {Date} date Date that we should transform.
	 * @param {string} format The basic format of the string.
	 * @return {Date} The string as a date object.
	 */
	var __toDate = function ( date, format ){
		// Default values set to midnight Jan 1 of the current year.
		var year = new Date().getFullYear(),
			month = 0,
			day = 1,
			hours = 0,
			minutes = 0,
			seconds = 0;

		// Positions of each date element within the source string.  Use to know
		// which backreference to check after a successful match.
		var yearPos = -1,
			monthPos = -1,
			dayPos = -1,
			hoursPos = -1,
			minutesPos = -1,
			secondsPos = -1,
			amPmPos = -1;

		var monthStyle = 'm',       // How we interpret the month, digits (M/m) or names (N/n)
			hoursStyle = 'h';       // How we interpret the hours, 12-hour (h) or 24-hour (r)

		var position = 1,           // Position of the current date element (year, month, day, etc.) in the source string
			pattern = '';           // Date pattern to be matched.

		// Remove extraneous whitespace from source string and format string.
		var str = date.replace( /\s+/g, ' ' );
		format = format.replace( /\s+/g, ' ' );

		// Loop throught the format string, and build the regex pattern
		// for extracting the date elements.
		for ( var i = 0, len = format.length; i < len; i++ ) {
			var c = format.charAt( i );
			switch ( c ) {
				case 'Y' :
					pattern += '(\\d{4})';
					yearPos = position++;
					break;
				case 'y' :
					pattern += '(\\d{2})';
					yearPos = position++;
					break;
				case 'M' :
				case 'm' :
					pattern += '(\\d{1,2})';
					monthPos = position++;
					monthStyle = 'm';
					break;
				case 'N' :
					pattern += '(' + __monthNames.join( '|' ) + ')';
					monthPos = position++;
					monthStyle = 'N';
					break;
				case 'n' :
					pattern += '(' + __shortMonthNames.join( '|' ) + ')';
					monthPos = position++;
					monthStyle = 'n';
					break;
				case 'D' :
				case 'd' :
					pattern += '(\\d{1,2})';
					dayPos = position++;
					break;
				case 'W' : // We'll match W, but won't do anything with it.
					pattern += '(' + __dayNames.join( '|' ) + ')';
					position++;
					break;
				case 'w' : // We'll match w, but won't do anything with it.
					pattern += '(' + __shortDayNames.join( '|' ) + ')';
					position++;
					break;
				case 'H' :
				case 'h' :
					pattern += '(\\d{1,2})';
					hoursPos = position++;
					hoursStyle = 'h';
					break;
				case 'R' :
				case 'r' :
					pattern += '(\\d{1,2})';
					hoursPos = position++;
					hoursStyle = 'r';
					break;
				case 'I' :
				case 'i' :
					pattern += '(\\d{1,2})';
					minutesPos = position++;
					break;
				case 'S' :
				case 's' :
					pattern += '(\\d{1,2})';
					secondsPos = position++;
					break;
				case 'A' :
				case 'a' :
					pattern += '(AM|am|PM|pm)';
					amPmPos = position++;
					break;
				default :
					pattern += (c == '^' ? format.charAt( ++i ) : c);
			}
		}

		// Pull out the date elements from the input string
		var matches = str.match( new RegExp( pattern ) );
		if ( !matches ) {
			return null;
		}

		// Now we have to interpret each of those parts...

		if ( yearPos > -1 ) {
			year = parseInt( matches[yearPos], 10 );
			year = (year < 50 ? year + 2000 : (year < 100 ? year + 1900 : year));
		}

		if ( monthPos > -1 ) {
			switch ( monthStyle ) {
				case 'm':
					month = parseInt( matches[monthPos], 10 ) - 1;    // JavaScript months are zero based, user input generally is not.
					if ( month > 11 )
						return null;
					break;
				case 'N':
					month = parseInt( __monthNumbers[matches[monthPos]], 10 );
					if ( isNaN( month ) )
						return null;
					break;
				case 'n':
					month = parseInt( __shortMonthNumbers[matches[monthPos]], 10 );
					if ( isNaN( month ) )
						return null;
					break;
			}
		}

		if ( dayPos > -1 ) {
			day = parseInt( matches[dayPos], 10 );
			if ( (day < 1) || (day > __daysInMonth( month, year )) )
				return null;
		}

		if ( hoursPos > -1 ) {
			hours = parseInt( matches[hoursPos], 10 );
			if ( hoursStyle == 'h' && (hours === 0 || hours > 12) )
				return null;
			else if ( hours > 23 )
				return null;
		}

		if ( minutesPos > -1 ) {
			minutes = parseInt( matches[minutesPos], 10 );
			if ( minutes > 59 )
				return null;
		}

		if ( secondsPos > -1 ) {
			seconds = parseInt( matches[secondsPos], 10 );
			if ( seconds > 59 )
				return null;
		}

		// Convert 12-hour time, if used, to 24-hour time.
		if ( amPmPos > -1 ) {
			var amPm = matches[amPmPos];
			if ( (amPm == 'pm' || amPm == 'PM') && (hours < 12) )
				hours += 12;
		}

		return new Date( year, month, day, hours, minutes, seconds );
	};


	/**
	 * Simple getElementByID function
	 * @param {string} id - id of HTML element
	 * @returns {HTMLElement}
	 * @private
	 */
	var __getElById = function ( id ){
		return document.getElementById( id );
	}

	/**
	 * Check is obj is array or not
	 * @param obj - element we should check
	 * @returns {boolean}
	 * @private
	 */
	var __isArray = function ( obj ){
		return Object.prototype.toString.call( obj ) == '[object Array]';
	};

	/**
	 * detects is defined array has some value
	 * @param array
	 * @param value
	 * @returns {number}
	 * @private
	 */
	var __inArray = function ( array, value ){
		var index = -1,
			length = array ? array.length : 0;
		while ( ++index < length ) {
			if ( array[index] === value ) {
				return index;
			}
		}
		return -1;
	};
	window.__inArray = __inArray;


	/**
	 * convert item to Array.
	 * @param el
	 * @returns {Array}
	 * @private
	 */
	var __toArray = function ( el ){
		return (!__isArray( el )) ? [el] : el;
	}

	/**
	 * convert rules object to string
	 * @param obj
	 * @param separator
	 * @returns {string}
	 * @private
	 */
	var __rulesStr = function ( obj, separator ){
		separator = separator || ' ';
		var str = separator;
		for ( var key in obj ) {
			var rules = obj[key];
			if ( __isArray( rules )){
				rules = __clearArray(rules);
			}
			if ( !rules ) {
				str += key + separator;
			} else if ( __isArray( rules ) ) {
				str += key + '[' + rules.join( ',' ) + ']' + separator; // TODO: rule values separator
			} else {
				str += key + rules + separator;
			}
		}
		str = str.substr( separator.length, str.length - separator.length * 2 );
		return str;
	};

	var __clearArray = function(arr){
		var new_arr = [];
		for (var i = 0, a_l = arr.length; i < a_l; i++) {
			if (arr[i]) {
				new_arr.push(arr[i]);
			}
		}
		return (new_arr && new_arr.length > 1) ? new_arr : new_arr[0];
	}

})( window, document );;
/*! device.js 0.1.61 */
(function(){var a,b,c,d,e,f,g,h,i,j;a=window.device,window.device={},c=window.document.documentElement,j=window.navigator.userAgent.toLowerCase(),device.ios=function(){return device.iphone()||device.ipod()||device.ipad()},device.iphone=function(){return d("iphone")},device.ipod=function(){return d("ipod")},device.ipad=function(){return d("ipad")},device.android=function(){return d("android")},device.androidPhone=function(){return device.android()&&d("mobile")},device.androidTablet=function(){return device.android()&&!d("mobile")},device.blackberry=function(){return d("blackberry")||d("bb10")||d("rim")},device.blackberryPhone=function(){return device.blackberry()&&!d("tablet")},device.blackberryTablet=function(){return device.blackberry()&&d("tablet")},device.windows=function(){return d("windows")},device.windowsPhone=function(){return device.windows()&&d("phone")},device.windowsTablet=function(){return device.windows()&&d("touch")&&!device.windowsPhone()},device.fxos=function(){return(d("(mobile;")||d("(tablet;"))&&d("; rv:")},device.fxosPhone=function(){return device.fxos()&&d("mobile")},device.fxosTablet=function(){return device.fxos()&&d("tablet")},device.meego=function(){return d("meego")},device.cordova=function(){return window.cordova&&"file:"===location.protocol},device.nodeWebkit=function(){return"object"==typeof window.process},device.mobile=function(){return device.androidPhone()||device.iphone()||device.ipod()||device.windowsPhone()||device.blackberryPhone()||device.fxosPhone()||device.meego()},device.tablet=function(){return device.ipad()||device.androidTablet()||device.blackberryTablet()||device.windowsTablet()||device.fxosTablet()},device.desktop=function(){return!device.tablet()&&!device.mobile()},device.portrait=function(){return window.innerHeight/window.innerWidth>1},device.landscape=function(){return window.innerHeight/window.innerWidth<1},device.noConflict=function(){return window.device=a,this},d=function(a){return-1!==j.indexOf(a)},f=function(a){var b;return b=new RegExp(a,"i"),c.className.match(b)},b=function(a){return f(a)?void 0:c.className+=" "+a},h=function(a){return f(a)?c.className=c.className.replace(a,""):void 0},device.ios()?device.ipad()?b("ios ipad tablet"):device.iphone()?b("ios iphone mobile"):device.ipod()&&b("ios ipod mobile"):b(device.android()?device.androidTablet()?"android tablet":"android mobile":device.blackberry()?device.blackberryTablet()?"blackberry tablet":"blackberry mobile":device.windows()?device.windowsTablet()?"windows tablet":device.windowsPhone()?"windows mobile":"desktop":device.fxos()?device.fxosTablet()?"fxos tablet":"fxos mobile":device.meego()?"meego mobile":device.nodeWebkit()?"node-webkit":"desktop"),device.cordova()&&b("cordova"),e=function(){return device.landscape()?(h("portrait"),b("landscape")):(h("landscape"),b("portrait"))},i="onorientationchange"in window,g=i?"orientationchange":"resize",window.addEventListener?window.addEventListener(g,e,!1):window.attachEvent?window.attachEvent(g,e):window[g]=e,e()}).call(this);;
/*! Copyright (c) 2011 Brandon Aaron (http://brandonaaron.net)
 * Licensed under the MIT License (LICENSE.txt).
 *
 * Thanks to: http://adomas.org/javascript-mouse-wheel/ for some pointers.
 * Thanks to: Mathias Bank(http://www.mathias-bank.de) for a scope bug fix.
 * Thanks to: Seamus Leahy for adding deltaX and deltaY
 *
 * Version: 3.0.6
 * 
 * Requires: 1.2.2+
 */
(function(a){function d(b){var c=b||window.event,d=[].slice.call(arguments,1),e=0,f=!0,g=0,h=0;return b=a.event.fix(c),b.type="mousewheel",c.wheelDelta&&(e=c.wheelDelta/120),c.detail&&(e=-c.detail/3),h=e,c.axis!==undefined&&c.axis===c.HORIZONTAL_AXIS&&(h=0,g=-1*e),c.wheelDeltaY!==undefined&&(h=c.wheelDeltaY/120),c.wheelDeltaX!==undefined&&(g=-1*c.wheelDeltaX/120),d.unshift(b,e,g,h),(a.event.dispatch||a.event.handle).apply(this,d)}var b=["DOMMouseScroll","mousewheel"];if(a.event.fixHooks)for(var c=b.length;c;)a.event.fixHooks[b[--c]]=a.event.mouseHooks;a.event.special.mousewheel={setup:function(){if(this.addEventListener)for(var a=b.length;a;)this.addEventListener(b[--a],d,!1);else this.onmousewheel=d},teardown:function(){if(this.removeEventListener)for(var a=b.length;a;)this.removeEventListener(b[--a],d,!1);else this.onmousewheel=null}},a.fn.extend({mousewheel:function(a){return a?this.bind("mousewheel",a):this.trigger("mousewheel")},unmousewheel:function(a){return this.unbind("mousewheel",a)}})})(jQuery)
;
/* jquery.simplr.smoothscroll version 1.0 copyright (c) 2012 https://github.com/simov/simplr-smoothscroll licensed under MIT */
;(function(e){"use strict";e.srSmoothscroll=function(t){var platform = window.navigator.platform; if ((platform === 'MacIntel' || platform === 'MacPPC')){return false}; var n=e.extend({step:170,speed:1000,ease:"swing"},t||{});var r=e(window),i=e(document),s=0,o=n.step,u=n.speed,a=r.height(),f=navigator.userAgent.indexOf("AppleWebKit")!==-1?e("body"):e("html"),l=false;e("body").mousewheel(function(e,t){l=true;if(t<0)s=s+a>=i.height()?s:s+=o;else s=s<=0?0:s-=o;f.stop().animate({scrollTop:s},u,n.ease,function(){l=false});return false});r.on("resize",function(e){a=r.height()}).on("scroll",function(e){if(!l)s=r.scrollTop()})}})(jQuery);
;

var warnedAbout = {};

// List of warnings already given; public read only
jQuery.migrateWarnings = [];

// Set to true to prevent console output; migrateWarnings still maintained
// jQuery.migrateMute = false;

// Show a message on the console so devs know we're active
if (!jQuery.migrateMute && window.console && window.console.log) {
	window.console.log("JQMIGRATE: Logging is active");
}

// Set to false to disable traces that appear with warnings
if (jQuery.migrateTrace === undefined) {
	jQuery.migrateTrace = true;
}

// Forget any warnings we've already given; public
jQuery.migrateReset = function() {
	warnedAbout = {};
	jQuery.migrateWarnings.length = 0;
};

function migrateWarn(msg) {
	var console = window.console;
	if (!warnedAbout[msg]) {
		warnedAbout[msg] = true;
		jQuery.migrateWarnings.push(msg);
		if (console && console.warn && !jQuery.migrateMute) {
			console.warn("JQMIGRATE: " + msg);
			if (jQuery.migrateTrace && console.trace) {
				console.trace();
			}
		}
	}
}

function migrateWarnProp(obj, prop, value, msg) {
	if (Object.defineProperty) {
		// On ES5 browsers (non-oldIE), warn if the code tries to get prop;
		// allow property to be overwritten in case some other plugin wants it
		try {
			Object.defineProperty(obj, prop, {
				configurable: true,
				enumerable: true,
				get: function() {
					migrateWarn(msg);
					return value;
				},
				set: function(newValue) {
					migrateWarn(msg);
					value = newValue;
				}
			});
			return;
		} catch(err) {
			// IE8 is a dope about Object.defineProperty, can't warn there
		}
	}

	// Non-ES5 (or broken) browser; just set the property
	jQuery._definePropertyBroken = true;
	obj[ prop ] = value;
}

if (document.compatMode === "BackCompat") {
	// jQuery has never supported or tested Quirks Mode
	migrateWarn("jQuery is not compatible with Quirks Mode");
};
