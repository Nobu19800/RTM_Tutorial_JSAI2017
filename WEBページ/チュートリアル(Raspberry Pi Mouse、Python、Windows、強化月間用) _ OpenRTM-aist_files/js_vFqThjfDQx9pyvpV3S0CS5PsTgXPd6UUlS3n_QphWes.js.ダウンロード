// $Id: jquery.textsize.js,v 1.3 2009/12/10 23:16:50 christianzwahlen Exp $

(function($) {
  $(document).ready(function(){
    $("a.ts_increase_variable").attr({ href: "#" });
    $("a.ts_decrease_variable").attr({ href: "#" });
    $("a.ts_normal_variable").attr({ href: "#" });
    $("a.ts_increase_fix").attr({ href: "#" });
    $("a.ts_decrease_fix").attr({ href: "#" });
    $("a.ts_normal_fix").attr({ href: "#" });
    function textsizeDisplayCalc(ts_v) {
      if (textsizeDisplay == 1) {
        ts_c = (100 * ts_v / textsizeNormal);
        return Math.round(ts_c);
      }
      else {
        return ts_v;
      }
    }
    function textsizeIncrease(ts_a, ts_b) {
      if (ts_a == textsizeMaximum) {
        return ts_a;
      }
      else {
        return 1*ts_a + 1*textsizeIncrement;
      }
    }
    function textsizeDecrease(ts_a, ts_b) {
      if (ts_a == textsizeMinimum) {
        return ts_a;
      }
      else {
        return 1*ts_a - 1*textsizeIncrement;
      }
    }
    function TSremoveBC(){
      var tsElement = $(textsizeElement + textsizeElementClass);
      var tsClasses = tsElement.attr('class').split(' ');
      for( var i in tsClasses ){
        if( tsClasses[i].substring(0,8) == 'textsize' ){
          tsElement.removeClass( tsClasses[i] );
          break;
        }
      }
    }
    function tsIncrease(){
      TSremoveBC();
      $("#textsize_current").empty();
      $("#textsize_current").append((textsizeNormalDisplay + textsizeIncrementDisplay) + '%');
      $("#textsize_current").attr({ title: textsizeCurrentText + ": " + (textsizeNormalDisplay + textsizeIncrementDisplay) + '%'});
      $(textsizeElement + textsizeElementClass).addClass('textsize-' + (textsizeNormal + textsizeIncrement));
      $(textsizeElement + textsizeElementClass).css("font-size", (textsizeNormal + textsizeIncrement) + "%");
      $.cookie('textsize', textsizeIncrease(textsizeNormalDisplay, textsizeIncrementDisplay), { expires: textsizeCookieExpires, path: textsizeCookieDomain});
      return false;
    }
    function tsDecrease(){
      TSremoveBC();
      $("#textsize_current").empty();
      $("#textsize_current").append((textsizeNormalDisplay - textsizeIncrementDisplay) + '%');
      $("#textsize_current").attr({ title: textsizeCurrentText + ": " + (textsizeNormalDisplay - textsizeIncrementDisplay) + '%'});
      $(textsizeElement + textsizeElementClass).addClass('textsize-' + (textsizeNormal - textsizeIncrement));
      $(textsizeElement + textsizeElementClass).css("font-size", (textsizeNormal - textsizeIncrement) + "%");
      $.cookie('textsize', textsizeDecrease(textsizeNormalDisplay, textsizeIncrementDisplay), { expires: textsizeCookieExpires, path: textsizeCookieDomain});
      return false;
    }
    function tsNormal(){
      TSremoveBC();
      $("#textsize_current").empty();
      $("#textsize_current").append(textsizeNormalDisplay + '%');
      $("#textsize_current").removeClass('error');
      $("#textsize_current").attr({ title: textsizeCurrentText + ": " + textsizeNormalDisplay + '%'});
      $(textsizeElement + textsizeElementClass).addClass('textsize-' + textsizeNormal);
      $(textsizeElement + textsizeElementClass).css("font-size", textsizeNormal + "%");
      $.cookie('textsize', textsizeNormal, { expires: textsizeCookieExpires, path: textsizeCookieDomain});
      return false;
    }
    function tsForm() {
      var ts_val = $("#edit-textsize-select").val();
      var ts_val_d = textsizeDisplayCalc($("#edit-textsize-select").val());
      TSremoveBC();
      $.cookie('textsize', ts_val, { expires: textsizeCookieExpires, path: textsizeCookieDomain});
      $(textsizeElement + textsizeElementClass).addClass("textsize-" + ts_val);
      $("#textsize_current").empty();
      $("#textsize_current").append(ts_val_d + '%');
      $("#textsize_current").attr({ title: textsizeCurrentText + ": " + ts_val_d + '%'});
      $(textsizeElement + textsizeElementClass).addClass('textsize-' + ts_val);
      $(textsizeElement + textsizeElementClass).css("font-size", ts_val + "%");
    }
    $("a.ts_increase_variable[href=#]").click(
      function (){
        if ($.cookie("textsize") && $.cookie("textsize") < textsizeMaximum) {
          TSremoveBC();
          $.cookie('textsize', textsizeIncrease($.cookie("textsize"), textsizeIncrement), { expires: textsizeCookieExpires, path: textsizeCookieDomain});
          $("#textsize_current").empty();
          $("#textsize_current").append( textsizeDisplayCalc($.cookie("textsize")) + '%');
          $("#textsize_current").attr({ title: textsizeCurrentText + ": " + textsizeDisplayCalc($.cookie("textsize")) + '%'});
          $("#textsize_current").removeClass('error');
          $(textsizeElement + textsizeElementClass).addClass('textsize-' + $.cookie("textsize"));
          $(textsizeElement + textsizeElementClass).css("font-size", $.cookie("textsize") + "%");
          return false;
        }
        else if ($.cookie("textsize") && ($.cookie("textsize") == textsizeMaximum) && textsizeReset == 0) {
          $("#textsize_current").empty();
          $("#textsize_current").append( '<abbr title="' + Drupal.t('Maximum') + '" class="textsize">' + Drupal.t('Max.') + '</abbr> ' + textsizeDisplayCalc(textsizeMaximum) + '%');
          $("#textsize_current").addClass('error');
          return false;
        }
        else if ($.cookie("textsize") && ($.cookie("textsize") == textsizeMaximum) && textsizeReset == 1) {
          tsNormal()
          return false;
        }
      }
    );
    $("a.ts_increase_fix[href=#]").click(
      function (){
        if ($.cookie("textsize") && $.cookie("textsize") < (textsizeNormal + textsizeIncrement)) {
          TSremoveBC();
          $.cookie('textsize', (textsizeNormal + textsizeIncrement), { expires: textsizeCookieExpires, path: textsizeCookieDomain});
          $("#textsize_current").empty();
          $("#textsize_current").append( textsizeDisplayCalc($.cookie("textsize")) + '%');
          $("#textsize_current").attr({ title: textsizeCurrentText + ": " + textsizeDisplayCalc($.cookie("textsize")) + '%'});
          $("#textsize_current").removeClass('error');
          $(textsizeElement + textsizeElementClass).addClass('textsize-' + (textsizeNormal + textsizeIncrement));
          $(textsizeElement + textsizeElementClass).css("font-size", (textsizeNormal + textsizeIncrement) + "%");
          return false;
        }
        else if ($.cookie("textsize") && $.cookie("textsize") == (textsizeNormal + textsizeIncrement)) {
          $("#textsize_current").empty();
          $("#textsize_current").append( '<abbr title="' + Drupal.t('Maximum') + '" class="textsize">' + Drupal.t('Max.') + '</abbr> ' + textsizeDisplayCalc((textsizeNormal + textsizeIncrement)) + '%');
          $("#textsize_current").addClass('error');
          return false;
        }
        else {
          tsIncrease()
        }
      }
    );
    $("a.ts_decrease_variable[href=#]").click(
      function (){
        if ($.cookie("textsize") && $.cookie("textsize") > textsizeMinimum) {
          TSremoveBC();
          $.cookie('textsize', textsizeDecrease($.cookie("textsize"), textsizeIncrement), { expires: textsizeCookieExpires, path: textsizeCookieDomain});
          $("#textsize_current").empty();
          $("#textsize_current").append( textsizeDisplayCalc($.cookie("textsize")) + '%');
          $("#textsize_current").attr({ title: textsizeCurrentText + ": " + textsizeDisplayCalc($.cookie("textsize")) + '%'});
          $("#textsize_current").removeClass('error');
          $(textsizeElement + textsizeElementClass).addClass('textsize-' + $.cookie("textsize"));
          $(textsizeElement + textsizeElementClass).css("font-size", $.cookie("textsize") + "%");
          return false;
        }
        else if ($.cookie("textsize") && ($.cookie("textsize") == textsizeMinimum) && textsizeReset == 0) {
          $("#textsize_current").empty();
          $("#textsize_current").append( '<abbr title="' + Drupal.t('Minimum') + '" class="textsize">' + Drupal.t('Min.') + '</abbr> ' + textsizeDisplayCalc(textsizeMinimum) + '%');
          $("#textsize_current").addClass('error');
          return false;
        }
        else if ($.cookie("textsize") && ($.cookie("textsize") == textsizeMinimum) && textsizeReset == 1) {
          tsNormal()
          return false;
        }
      }
    );
    $("a.ts_decrease_fix[href=#]").click(
      function (){
        if ($.cookie("textsize") && $.cookie("textsize") > (textsizeNormal - textsizeIncrement)) {
          TSremoveBC();
          $.cookie('textsize', (textsizeNormal - textsizeIncrement), { expires: textsizeCookieExpires, path: textsizeCookieDomain});
          $("#textsize_current").empty();
          $("#textsize_current").append( textsizeDisplayCalc($.cookie("textsize")) + '%');
          $("#textsize_current").attr({ title: textsizeCurrentText + ": " + textsizeDisplayCalc($.cookie("textsize")) + '%'});
          $("#textsize_current").removeClass('error');
          $(textsizeElement + textsizeElementClass).addClass('textsize-' + (textsizeNormal - textsizeIncrement));
          $(textsizeElement + textsizeElementClass).css("font-size", (textsizeNormal - textsizeIncrement) + "%");
          return false;
        }
        else if ($.cookie("textsize") && $.cookie("textsize") == (textsizeNormal - textsizeIncrement)) {
          $("#textsize_current").empty();
          $("#textsize_current").append( '<abbr title="' + Drupal.t('Minimum') + '" class="textsize">' + Drupal.t('Min.') + '</abbr> ' + textsizeDisplayCalc((textsizeNormal - textsizeIncrement)) + '%');
          $("#textsize_current").addClass('error');
          return false;
        }
        else {
          tsDecrease()
        }
      }
    );
    $("a.ts_normal_variable[href=#]").click(
      function (){
        tsNormal();
        return false;
      }
    );
    $("a.ts_normal_fix[href=#]").click(
      function (){
        tsNormal();
        return false;
      }
    );
    $("#edit-textsize-select").change(tsForm);
    $("#edit-textsize-submit").hide();
    $("img.ts_rollover").hover(
      function(){
        if($(this).attr("src").indexOf("16_hover") == -1) {
          var newSrc = $(this).attr("src").replace("16.gif","16_hover.gif#hover");
          $(this).attr("src",newSrc);
        }
      },
      function(){
        if($(this).attr("src").indexOf("16_hover.gif#hover") != -1) {
          var oldSrc = $(this).attr("src").replace("16_hover.gif#hover","16.gif");
          $(this).attr("src",oldSrc);
        }
        else if($(this).attr("src").indexOf("16_focus.gif#focus") != -1) {
          var oldSrc = $(this).attr("src").replace("16_focus.gif#focus","16.gif");
          $(this).attr("src",oldSrc);
        }
      }
    );
    $("a.ts_rollover").focus(
      function(){
        var tsIMG = $(this).children("img");
        if($(tsIMG).attr("src").indexOf("16_hover.gif#hover") != -1) {
          var newSrc = $(tsIMG).attr("src").replace("16_hover.gif#hover","16_focus.gif#focus");
          $(tsIMG).attr("src",newSrc);
        }
      }
    );
  });
})(jQuery);
;

/**
 * Cookie plugin 1.0
 *
 * Copyright (c) 2006 Klaus Hartl (stilbuero.de)
 * Dual licensed under the MIT and GPL licenses:
 * http://www.opensource.org/licenses/mit-license.php
 * http://www.gnu.org/licenses/gpl.html
 *
 */
jQuery.cookie=function(b,j,m){if(typeof j!="undefined"){m=m||{};if(j===null){j="";m.expires=-1}var e="";if(m.expires&&(typeof m.expires=="number"||m.expires.toUTCString)){var f;if(typeof m.expires=="number"){f=new Date();f.setTime(f.getTime()+(m.expires*24*60*60*1000))}else{f=m.expires}e="; expires="+f.toUTCString()}var l=m.path?"; path="+(m.path):"";var g=m.domain?"; domain="+(m.domain):"";var a=m.secure?"; secure":"";document.cookie=[b,"=",encodeURIComponent(j),e,l,g,a].join("")}else{var d=null;if(document.cookie&&document.cookie!=""){var k=document.cookie.split(";");for(var h=0;h<k.length;h++){var c=jQuery.trim(k[h]);if(c.substring(0,b.length+1)==(b+"=")){d=decodeURIComponent(c.substring(b.length+1));break}}}return d}};
;
(function() {
	var MutationObserver, Util, WeakMap,
		__bind = function(fn, me){ return function(){ return fn.apply(me, arguments); }; },
		__indexOf = [].indexOf || function(item) { for (var i = 0, l = this.length; i < l; i++) { if (i in this && this[i] === item) return i; } return -1; };

	Util = (function() {
		function Util() {}

		Util.prototype.extend = function(custom, defaults) {
			var key, value;
			for (key in custom) {
				value = custom[key];
				if (value != null) {
					defaults[key] = value;
				}
			}
			return defaults;
		};

		Util.prototype.isMobile = function(agent) {
			return /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(agent);
		};

		return Util;

	})();

	WeakMap = this.WeakMap || this.MozWeakMap || (WeakMap = (function() {
		function WeakMap() {
			this.keys = [];
			this.values = [];
		}

		WeakMap.prototype.get = function(key) {
			var i, item, _i, _len, _ref;
			_ref = this.keys;
			for (i = _i = 0, _len = _ref.length; _i < _len; i = ++_i) {
				item = _ref[i];
				if (item === key) {
					return this.values[i];
				}
			}
		};

		WeakMap.prototype.set = function(key, value) {
			var i, item, _i, _len, _ref;
			_ref = this.keys;
			for (i = _i = 0, _len = _ref.length; _i < _len; i = ++_i) {
				item = _ref[i];
				if (item === key) {
					this.values[i] = value;
					return;
				}
			}
			this.keys.push(key);
			return this.values.push(value);
		};

		return WeakMap;

	})());

	MutationObserver = this.MutationObserver || this.WebkitMutationObserver || this.MozMutationObserver || (MutationObserver = (function() {
		function MutationObserver() {
			console.warn('MutationObserver is not supported by your browser.');
			console.warn('WOW.js cannot detect dom mutations, please call .sync() after loading new content.');
		}

		MutationObserver.notSupported = true;

		MutationObserver.prototype.observe = function() {};

		return MutationObserver;

	})());

	this.WOW = (function() {
		WOW.prototype.defaults = {
			boxClass: 'wow',
			animateClass: 'animated',
			offset: 0,
			mobile: true,
			live: true
		};

		function WOW(options) {
			if (options == null) {
				options = {};
			}
			this.scrollCallback = __bind(this.scrollCallback, this);
			this.scrollHandler = __bind(this.scrollHandler, this);
			this.start = __bind(this.start, this);
			this.scrolled = true;
			this.config = this.util().extend(options, this.defaults);
			this.animationNameCache = new WeakMap();
		}

		WOW.prototype.init = function() {
			var _ref;
			this.element = window.document.documentElement;
			if ((_ref = document.readyState) === "interactive" || _ref === "complete") {
				this.start();
			} else {
				document.addEventListener('DOMContentLoaded', this.start);
			}
			return this.finished = [];
		};

		WOW.prototype.start = function() {
			var box, _i, _len, _ref;
			this.stopped = false;
			this.boxes = this.element.getElementsByClassName(this.config.boxClass);
			this.all = (function() {
				var _i, _len, _ref, _results;
				_ref = this.boxes;
				_results = [];
				for (_i = 0, _len = _ref.length; _i < _len; _i++) {
					box = _ref[_i];
					_results.push(box);
				}
				return _results;
			}).call(this);
			if (this.boxes.length) {
				if (this.disabled()) {
					this.resetStyle();
				} else {
					_ref = this.boxes;
					for (_i = 0, _len = _ref.length; _i < _len; _i++) {
						box = _ref[_i];
						this.applyStyle(box, true);
					}
					window.addEventListener('scroll', this.scrollHandler, false);
					window.addEventListener('resize', this.scrollHandler, false);
					this.interval = setInterval(this.scrollCallback, 50);
				}
			}
			if (this.config.live) {
				return new MutationObserver((function(_this) {
					return function(records) {
						var node, record, _j, _len1, _results;
						_results = [];
						for (_j = 0, _len1 = records.length; _j < _len1; _j++) {
							record = records[_j];
							_results.push((function() {
								var _k, _len2, _ref1, _results1;
								_ref1 = record.addedNodes || [];
								_results1 = [];
								for (_k = 0, _len2 = _ref1.length; _k < _len2; _k++) {
									node = _ref1[_k];
									_results1.push(this.doSync(node));
								}
								return _results1;
							}).call(_this));
						}
						return _results;
					};
				})(this)).observe(document.body, {
					childList: true,
					subtree: true
				});
			}
		};

		WOW.prototype.stop = function() {
			this.stopped = true;
			window.removeEventListener('scroll', this.scrollHandler, false);
			window.removeEventListener('resize', this.scrollHandler, false);
			if (this.interval != null) {
				return clearInterval(this.interval);
			}
		};

		WOW.prototype.sync = function(element) {
			if (MutationObserver.notSupported) {
				return this.doSync(this.element);
			}
		};

		WOW.prototype.doSync = function(element) {
			var box, _i, _len, _ref, _results;
			if (!this.stopped) {
				element || (element = this.element);
				element = element.parentNode || element;
				_ref = element.getElementsByClassName(this.config.boxClass);
				_results = [];
				for (_i = 0, _len = _ref.length; _i < _len; _i++) {
					box = _ref[_i];
					if (__indexOf.call(this.all, box) < 0) {
						this.applyStyle(box, true);
						this.boxes.push(box);
						this.all.push(box);
						_results.push(this.scrolled = true);
					} else {
						_results.push(void 0);
					}
				}
				return _results;
			}
		};

		WOW.prototype.show = function(box) {
			this.applyStyle(box);
			return box.className = "" + box.className + " " + this.config.animateClass;
		};

		WOW.prototype.applyStyle = function(box, hidden) {
			var delay, duration, iteration;
			duration = box.getAttribute('data-wow-duration');
			delay = box.getAttribute('data-wow-delay');
			iteration = box.getAttribute('data-wow-iteration');
			return this.animate((function(_this) {
				return function() {
					return _this.customStyle(box, hidden, duration, delay, iteration);
				};
			})(this));
		};

		WOW.prototype.animate = (function() {
			if ('requestAnimationFrame' in window) {
				return function(callback) {
					return window.requestAnimationFrame(callback);
				};
			} else {
				return function(callback) {
					return callback();
				};
			}
		})();

		WOW.prototype.resetStyle = function() {
			var box, _i, _len, _ref, _results;
			_ref = this.boxes;
			_results = [];
			for (_i = 0, _len = _ref.length; _i < _len; _i++) {
				box = _ref[_i];
				_results.push(box.setAttribute('style', 'visibility: visible;'));
			}
			return _results;
		};

		WOW.prototype.customStyle = function(box, hidden, duration, delay, iteration) {
			if (hidden) {
				this.cacheAnimationName(box);
			}
			box.style.visibility = hidden ? 'hidden' : 'visible';
			if (duration) {
				this.vendorSet(box.style, {
					animationDuration: duration
				});
			}
			if (delay) {
				this.vendorSet(box.style, {
					animationDelay: delay
				});
			}
			if (iteration) {
				this.vendorSet(box.style, {
					animationIterationCount: iteration
				});
			}
			this.vendorSet(box.style, {
				animationName: hidden ? 'none' : this.cachedAnimationName(box)
			});
			return box;
		};

		WOW.prototype.vendors = ["moz", "webkit"];

		WOW.prototype.vendorSet = function(elem, properties) {
			var name, value, vendor, _results;
			_results = [];
			for (name in properties) {
				value = properties[name];
				elem["" + name] = value;
				_results.push((function() {
					var _i, _len, _ref, _results1;
					_ref = this.vendors;
					_results1 = [];
					for (_i = 0, _len = _ref.length; _i < _len; _i++) {
						vendor = _ref[_i];
						_results1.push(elem["" + vendor + (name.charAt(0).toUpperCase()) + (name.substr(1))] = value);
					}
					return _results1;
				}).call(this));
			}
			return _results;
		};

		WOW.prototype.vendorCSS = function(elem, property) {
			var result, style, vendor, _i, _len, _ref;
			style = window.getComputedStyle(elem);
			result = style.getPropertyCSSValue(property);
			_ref = this.vendors;
			for (_i = 0, _len = _ref.length; _i < _len; _i++) {
				vendor = _ref[_i];
				result = result || style.getPropertyCSSValue("-" + vendor + "-" + property);
			}
			return result;
		};

		WOW.prototype.animationName = function(box) {
			var animationName;
			try {
				animationName = this.vendorCSS(box, 'animation-name').cssText;
			} catch (_error) {
				animationName = window.getComputedStyle(box).getPropertyValue('animation-name');
			}
			if (animationName === 'none') {
				return '';
			} else {
				return animationName;
			}
		};

		WOW.prototype.cacheAnimationName = function(box) {
			return this.animationNameCache.set(box, this.animationName(box));
		};

		WOW.prototype.cachedAnimationName = function(box) {
			return this.animationNameCache.get(box);
		};

		WOW.prototype.scrollHandler = function() {
			return this.scrolled = true;
		};

		WOW.prototype.scrollCallback = function() {
			var box;
			if (this.scrolled) {
				this.scrolled = false;
				this.boxes = (function() {
					var _i, _len, _ref, _results;
					_ref = this.boxes;
					_results = [];
					for (_i = 0, _len = _ref.length; _i < _len; _i++) {
						box = _ref[_i];
						if (!(box)) {
							continue;
						}
						if (this.isVisible(box)) {
							this.show(box);
							continue;
						}
						_results.push(box);
					}
					return _results;
				}).call(this);
				if (!(this.boxes.length || this.config.live)) {
					return this.stop();
				}
			}
		};

		WOW.prototype.offsetTop = function(element) {
			var top;
			while (element.offsetTop === void 0) {
				element = element.parentNode;
			}
			top = element.offsetTop;
			while (element = element.offsetParent) {
				top += element.offsetTop;
			}
			return top;
		};

		WOW.prototype.isVisible = function(box) {
			var bottom, offset, top, viewBottom, viewTop;
			offset = box.getAttribute('data-wow-offset') || this.config.offset;
			viewTop = window.pageYOffset;
			viewBottom = viewTop + this.element.clientHeight - offset;
			top = this.offsetTop(box);
			bottom = top + box.clientHeight;
			return top <= viewBottom && bottom >= viewTop;
		};

		WOW.prototype.util = function() {
			return this._util || (this._util = new Util());
		};

		WOW.prototype.disabled = function() {
			return !this.config.mobile && this.util().isMobile(navigator.userAgent);
		};

		return WOW;

	})();

}).call(this);

jQuery(document).ready(function() {
	if (jQuery(window).width() > 995 ) {
		new WOW().init();
	}
});
(function ($) {

/**
 * Attaches double-click behavior to toggle full path of Krumo elements.
 */
Drupal.behaviors.devel = {
  attach: function (context, settings) {

    // Add hint to footnote
    $('.krumo-footnote .krumo-call').once().before('<img style="vertical-align: middle;" title="Click to expand. Double-click to show path." src="' + settings.basePath + 'misc/help.png"/>');

    var krumo_name = [];
    var krumo_type = [];

    function krumo_traverse(el) {
      krumo_name.push($(el).html());
      krumo_type.push($(el).siblings('em').html().match(/\w*/)[0]);

      if ($(el).closest('.krumo-nest').length > 0) {
        krumo_traverse($(el).closest('.krumo-nest').prev().find('.krumo-name'));
      }
    }

    $('.krumo-child > div:first-child', context).dblclick(
      function(e) {
        if ($(this).find('> .krumo-php-path').length > 0) {
          // Remove path if shown.
          $(this).find('> .krumo-php-path').remove();
        }
        else {
          // Get elements.
          krumo_traverse($(this).find('> a.krumo-name'));

          // Create path.
          var krumo_path_string = '';
          for (var i = krumo_name.length - 1; i >= 0; --i) {
            // Start element.
            if ((krumo_name.length - 1) == i)
              krumo_path_string += '$' + krumo_name[i];

            if (typeof krumo_name[(i-1)] !== 'undefined') {
              if (krumo_type[i] == 'Array') {
                krumo_path_string += "[";
                if (!/^\d*$/.test(krumo_name[(i-1)]))
                  krumo_path_string += "'";
                krumo_path_string += krumo_name[(i-1)];
                if (!/^\d*$/.test(krumo_name[(i-1)]))
                  krumo_path_string += "'";
                krumo_path_string += "]";
              }
              if (krumo_type[i] == 'Object')
                krumo_path_string += '->' + krumo_name[(i-1)];
            }
          }
          $(this).append('<div class="krumo-php-path" style="font-family: Courier, monospace; font-weight: bold;">' + krumo_path_string + '</div>');

          // Reset arrays.
          krumo_name = [];
          krumo_type = [];
        }
      }
    );
  }
};

})(jQuery);
;
(function($) {
  $(function() {
    var settings = Drupal.settings.node_helper;
    /**/console.log(settings);
 
    // settings.simplify_the_multi_field.
    if (settings.simplify_the_multi_field['#value'].length) {
      var items = settings.simplify_the_multi_field['#value'].replace(/[\r\n]+/, ',').split(',');
      for (var i = 0; i < items.length; i++) {
        var id = items[i].split(':')[0].replace('_', '-');
        $('#' + id + '-und-0-multi-field-wrapper').each(function() {
          var error = '.messages.error.messages-inline';
          if ($(this).find(error) && $(this).find(error).length) {
            $(this).find(error).addClass("hidden");
            $(this).parent().parent().parent().append(
              '<div class="clearfix"></div>' +
              '<div class="messages error messages-inline">' + $(this).find(error).html() + '</div>'
            );
          }
        });
      }
    }

  });
}) (jQuery);
;
(function ($) {

Drupal.googleanalytics = {};

$(document).ready(function() {

  // Attach mousedown, keyup, touchstart events to document only and catch
  // clicks on all elements.
  $(document.body).bind("mousedown keyup touchstart", function(event) {

    // Catch the closest surrounding link of a clicked element.
    $(event.target).closest("a,area").each(function() {

      // Is the clicked URL internal?
      if (Drupal.googleanalytics.isInternal(this.href)) {
        // Skip 'click' tracking, if custom tracking events are bound.
        if ($(this).is('.colorbox') && (Drupal.settings.googleanalytics.trackColorbox)) {
          // Do nothing here. The custom event will handle all tracking.
          //console.info("Click on .colorbox item has been detected.");
        }
        // Is download tracking activated and the file extension configured for download tracking?
        else if (Drupal.settings.googleanalytics.trackDownload && Drupal.googleanalytics.isDownload(this.href)) {
          // Download link clicked.
          ga("send", {
            "hitType": "event",
            "eventCategory": "Downloads",
            "eventAction": Drupal.googleanalytics.getDownloadExtension(this.href).toUpperCase(),
            "eventLabel": Drupal.googleanalytics.getPageUrl(this.href),
            "transport": "beacon"
          });
        }
        else if (Drupal.googleanalytics.isInternalSpecial(this.href)) {
          // Keep the internal URL for Google Analytics website overlay intact.
          ga("send", {
            "hitType": "pageview",
            "page": Drupal.googleanalytics.getPageUrl(this.href),
            "transport": "beacon"
          });
        }
      }
      else {
        if (Drupal.settings.googleanalytics.trackMailto && $(this).is("a[href^='mailto:'],area[href^='mailto:']")) {
          // Mailto link clicked.
          ga("send", {
            "hitType": "event",
            "eventCategory": "Mails",
            "eventAction": "Click",
            "eventLabel": this.href.substring(7),
            "transport": "beacon"
          });
        }
        else if (Drupal.settings.googleanalytics.trackOutbound && this.href.match(/^\w+:\/\//i)) {
          if (Drupal.settings.googleanalytics.trackDomainMode !== 2 || (Drupal.settings.googleanalytics.trackDomainMode === 2 && !Drupal.googleanalytics.isCrossDomain(this.hostname, Drupal.settings.googleanalytics.trackCrossDomains))) {
            // External link clicked / No top-level cross domain clicked.
            ga("send", {
              "hitType": "event",
              "eventCategory": "Outbound links",
              "eventAction": "Click",
              "eventLabel": this.href,
              "transport": "beacon"
            });
          }
        }
      }
    });
  });

  // Track hash changes as unique pageviews, if this option has been enabled.
  if (Drupal.settings.googleanalytics.trackUrlFragments) {
    window.onhashchange = function() {
      ga("send", {
        "hitType": "pageview",
        "page": location.pathname + location.search + location.hash
      });
    };
  }

  // Colorbox: This event triggers when the transition has completed and the
  // newly loaded content has been revealed.
  if (Drupal.settings.googleanalytics.trackColorbox) {
    $(document).bind("cbox_complete", function () {
      var href = $.colorbox.element().attr("href");
      if (href) {
        ga("send", {
          "hitType": "pageview",
          "page": Drupal.googleanalytics.getPageUrl(href)
        });
      }
    });
  }

});

/**
 * Check whether the hostname is part of the cross domains or not.
 *
 * @param string hostname
 *   The hostname of the clicked URL.
 * @param array crossDomains
 *   All cross domain hostnames as JS array.
 *
 * @return boolean
 */
Drupal.googleanalytics.isCrossDomain = function (hostname, crossDomains) {
  /**
   * jQuery < 1.6.3 bug: $.inArray crushes IE6 and Chrome if second argument is
   * `null` or `undefined`, http://bugs.jquery.com/ticket/10076,
   * https://github.com/jquery/jquery/commit/a839af034db2bd934e4d4fa6758a3fed8de74174
   *
   * @todo: Remove/Refactor in D8
   */
  if (!crossDomains) {
    return false;
  }
  else {
    return $.inArray(hostname, crossDomains) > -1 ? true : false;
  }
};

/**
 * Check whether this is a download URL or not.
 *
 * @param string url
 *   The web url to check.
 *
 * @return boolean
 */
Drupal.googleanalytics.isDownload = function (url) {
  var isDownload = new RegExp("\\.(" + Drupal.settings.googleanalytics.trackDownloadExtensions + ")([\?#].*)?$", "i");
  return isDownload.test(url);
};

/**
 * Check whether this is an absolute internal URL or not.
 *
 * @param string url
 *   The web url to check.
 *
 * @return boolean
 */
Drupal.googleanalytics.isInternal = function (url) {
  var isInternal = new RegExp("^(https?):\/\/" + window.location.host, "i");
  return isInternal.test(url);
};

/**
 * Check whether this is a special URL or not.
 *
 * URL types:
 *  - gotwo.module /go/* links.
 *
 * @param string url
 *   The web url to check.
 *
 * @return boolean
 */
Drupal.googleanalytics.isInternalSpecial = function (url) {
  var isInternalSpecial = new RegExp("(\/go\/.*)$", "i");
  return isInternalSpecial.test(url);
};

/**
 * Extract the relative internal URL from an absolute internal URL.
 *
 * Examples:
 * - http://mydomain.com/node/1 -> /node/1
 * - http://example.com/foo/bar -> http://example.com/foo/bar
 *
 * @param string url
 *   The web url to check.
 *
 * @return string
 *   Internal website URL
 */
Drupal.googleanalytics.getPageUrl = function (url) {
  var extractInternalUrl = new RegExp("^(https?):\/\/" + window.location.host, "i");
  return url.replace(extractInternalUrl, '');
};

/**
 * Extract the download file extension from the URL.
 *
 * @param string url
 *   The web url to check.
 *
 * @return string
 *   The file extension of the passed url. e.g. "zip", "txt"
 */
Drupal.googleanalytics.getDownloadExtension = function (url) {
  var extractDownloadextension = new RegExp("\\.(" + Drupal.settings.googleanalytics.trackDownloadExtensions + ")([\?#].*)?$", "i");
  var extension = extractDownloadextension.exec(url);
  return (extension === null) ? '' : extension[1];
};

})(jQuery);
;
