/**
 * 滑块验证
 * @author good_idea
 * @date 2019年1月11日 上午10:48:41
 */
layui.define(["jquery", "layer", "form"], function (exports) {
	"use strict";
	var $ = layui.jquery,
		form = layui.form,
		layer = layui.layer,
		device = layui.device(),
		sliderVerify = {
			read: (function () {
				var css =
					".slider-item{height:38px;line-height:38px;background-color:#d0d0d0;position:relative;border: 1px solid white;}.slider-bg{position:absolute;width:40px;height:100%;z-index:100}.slider-btn{width:40px;height:96%;position:absolute;border:1px solid #ccc;cursor:move;text-align:center;background-color:#fff;user-select:none;color:#666;z-index:120}.slider-btn-success{font-size:26px}.slider-text{position:absolute;text-align:center;width:100%;height:100%;user-select:none;font-size:14px;color:#fff;z-index:120}.slider-error{animation:glow 800ms ease-out infinite alternate;}@keyframes glow{0%{border-color:#e6e6e6}100%{border-color:#ff5722}}",
					style = document.createElement("style");
				style.innerHTML = css;
				style.type = "text/css";
				($("head link:last")[0] && $("head link:last").after(style)) ||
					$("head").append(style);
			})()
		},
		dom = function (d) {
			return d[0];
		},
		thisSliderVerify = function () {
			var that = this;
			return {
				isOk: function () {
					return that.isOk.call(that);
				},
				reset: function () {
					return that.reset.call(that);
				},
				version: '1.7.1'
			};
		},
		MOD_NAME = "sliderVerify",
		MOD_BTN = "slider-btn",
		MOD_BG = "slider-bg",
		MOD_TEXT = "slider-text",
		MOD_NEXT = "layui-icon-next",
		MOD_OK = "layui-icon-ok-circle",
		MOD_BTN_SUCCESS = "slider-btn-success",
		MOD_DEFAULT_BG = "layui-bg-green",
		MOD_ERROR_BORDER = "slider-error",
		MOD_CONFIG_TEXT = "请拖动滑块验证",
		MOD_CONFIG_SUCCESS = "验证通过",
		Class = function (option) {
			var that = this;
			that.config = $.extend({}, that.config, option);
			that.render();
		};

	//默认配置
	Class.prototype.config = {
		elem: "",
		onOk: null,
		isOk: false,
		isAutoVerify: true,
		timer: null,
		bg: MOD_DEFAULT_BG, //默认滑块颜色
		text: MOD_CONFIG_TEXT
	};

	Class.prototype.render = function () {
		var that = this,
			option = that.config,
			elem = $(option.elem);
		if (!elem[0]) return;
		if (option.domid) option.domid.remove();
		option.domid = that.createIdNum();
		var sliderDom = $(
			[
				'<div id="' +
				option.domid +
				'"' +
				(option.isAutoVerify ? 'lay-verify="sliderVerify"' : "") +
				'class="slider-item">',
				'<div class="' + MOD_BG + " " + option.bg + '"></div>',
				'<div class="' + MOD_TEXT + '">' + option.text + "</div>",
				'<div class="' + MOD_BTN + ' layui-icon layui-icon-next"></div>'
			].join("")
		);
		elem.hide().after(sliderDom);
		option.domid = $("#" + option.domid);

		that.events();
		//自动验证
		if (option.isAutoVerify) {
			form.verify({
				sliderVerify: function (value, dom) {
					if (!value) {
						dom.classList.add(MOD_ERROR_BORDER);
						return option.text;
					}
				}
			});
		}
	};
	Class.prototype.isMobile = function () {
		return (
			device.os == "ios" ||
			device.os == "android" ||
			device.android ||
			device.ios
		) || (device.weixin && typeof device.weixin === Boolean);
	};
	Class.prototype.createIdNum = function () {
		return (
			MOD_NAME +
			(+new Date()).toString() +
			Math.random()
				.toString()
				.substr(2, 7)
		);
	};
	//验证是否验证成功
	Class.prototype.isOk = function () {
		return this.config.isOk;
	};

	Class.prototype.error = function (msg) {
		return layer.msg(msg, {
			icon: 5
		});
	};

	Class.prototype.distance = function () {
		var container = this.config.container;
		return container.box.offsetWidth - container.btn.offsetWidth; //滑动成功的宽度（距离）
	};

	//重置组件
	Class.prototype.reset = function () {
		this.config.isOk = false;
		return this.render();
	};

	//重置
	Class.prototype.resize = function (distance) {
		var that = this,
			container = that.config.container;
		var distance = distance || that.distance();
		container.btn.style.left = distance + "px";
		container.bg.style.width = distance + "px";
	};

	//取消动画
	Class.prototype.cancelTransition = function () {
		var container = this.config.container;
		this.config.domid[0].classList.remove(MOD_ERROR_BORDER);
		container.btn.style.transition = "";
		container.bg.style.transition = "";
	};
	//按下
	Class.prototype.down = function (e) {
		var that = this,
			option = that.config,
			container = option.container,
			e = e || window.event,
			//按下的坐标
			downX = e.clientX || e.touches[0].clientX;
		//每次将过渡去掉
		that.cancelTransition();
		var move = function (e) {
			that.move(downX, e);
		};
		that.events.move = move;
		//mobile移动
		if (that.isMobile()) {

			document.addEventListener("touchmove", that.events.move);
		} else {
			//pc移动
			document.onmousemove = move;
		}
		//处理部分浏览器滑动时左右翻页
		if(navigator.userAgent.indexOf("UCBrowser") > -1){
			e.preventDefault()
		}
	};
	//移动
	Class.prototype.move = function (down, e) {
		var that = this,
			option = that.config,
			container = option.container;
		var e = e || window.event;
		//鼠标移动后的水平位置
		var moveX = e.clientX || e.touches[0].clientX;
		//鼠标水平位置的偏移量（鼠标移动时的位置 - 鼠标按下时的位置）
		var offsetX = moveX - down;

		//判断一下：鼠标水平移动的距离 与 滑动成功的距离 之间的关系
		if (offsetX > container.distance) {
			offsetX = container.distance; //如果滑过了终点，就将它停留在终点位置
		} else if (offsetX < 0) {
			offsetX = 0; //滑到了起点的左侧，将它重置为起点位置
		}
		container.btn.style.left = offsetX + "px";
		container.bg.style.width = offsetX + "px";

		//鼠标的水平移动距离 = 滑动成功的宽度
		if (offsetX == container.distance) {
			//1.滑动成功后的样式
			container.text.innerHTML = MOD_CONFIG_SUCCESS;
			var com = window.getComputedStyle
				? window.getComputedStyle(container.bg, null)
				: container.bg.currentStyle;
			container.btn.style.border = "1px solid " + com.backgroundColor;
			container.btn.style.color = com.backgroundColor;
			container.btn.classList.remove(MOD_NEXT);
			container.btn.classList.add(MOD_OK, MOD_BTN_SUCCESS);
			option.isOk = true;
			container.box.value = true;
			//成功后，清除掉鼠标按下事件和移动事件（因为移动时并不会涉及到鼠标松开事件）
			//干掉mobile事件
			if (that.isMobile()) {
				container.btn.removeEventListener(
					"touchstart",
					that.events.down,
					false
				);
				document.removeEventListener(
					"touchmove",
					that.events.move,
					false
				);
			} else {
				container.btn.onmousedown = null;
				document.onmousemove = null;
			}
			//最后调用回调
			option.onOk && typeof option.onOk == "function" && option.onOk();
			return;
		}
		var seup = function (e) {
			that.stop(e);
		};
		that.events.seup = seup;
		if (that.isMobile()) {
			document.addEventListener("touchend", seup);
		} else {
			document.onmouseup = seup;
		}
	};
	//放开
	Class.prototype.stop = function (e) {
		var that = this,
			option = that.config,
			container = option.container;
		//鼠标松开，如果滑到了终点，则验证通过
		if (that.isOk()) {
			return;
		} else {
			container.btn.style.left = 0;
			container.bg.style.width = 0;
			container.btn.style.transition = "left 1s";
			container.bg.style.transition = "width 1s";
		}
		//鼠标松开了，不需要拖动就清除鼠标移动和松开事件。
		document.onmousemove = null;
		document.onmouseup = null;
		if (that.isMobile()) {
			document.removeEventListener("touchmove", that.events.move, false);
			document.removeEventListener("touchend", that.events.seup, false);
		}
	};
	//事件
	Class.prototype.events = function () {
		var that = this,
			option = that.config;
		if (!option.domid) return that.error("创建滑块验证失败");

		var btn = option.domid.find("." + MOD_BTN),
			bg = option.domid.find("." + MOD_BG),
			text = option.domid.find("." + MOD_TEXT),
			container = {
				box: dom(option.domid),
				btn: dom(btn),
				bg: dom(bg),
				text: dom(text)
			};
		option.container = container;
		container.distance = that.distance();
		var down = function (e) {
			that.down(e);
		};
		that.events.down = down;
		if (that.isMobile()) {
			container.btn.addEventListener("touchstart", that.events.down);
		} else {
			container.btn.onmousedown = down;
		}
		var $dom = $(window);
		$dom.on("resize", option.domid, function () {
			if (that.config.isOk) {
				//重新计算页面被拉伸
				that.resize();
			}else{
				//解决持续拉伸页面可能存在卡的问题
				clearTimeout(option.timer);
				option.timer = setTimeout(function () {
					that.render();
				}, 400)
			}
		});
	};

	sliderVerify.render = function (option) {
		var inst = new Class(option);
		return thisSliderVerify.call(inst);
	};

	exports(MOD_NAME, sliderVerify);
});
