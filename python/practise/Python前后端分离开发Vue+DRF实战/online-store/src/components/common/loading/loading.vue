<template>
    <div class="pio-loading2" v-if="flag">
       <div class="pio-loading2-box">
           <div class="pio-spinner"></div>
           <div class="pio-spinner"></div>
           <h6 class="pio-h7 pio-class-b">{{text}}</h6>
       </div>
   </div>
</template>
<script>
	export default {      
    }
</script>
<style scoped>
	.pio-loading2 {
	  width: 100%;
	  height: 100%;
	  position: absolute;
	  top: 0px;
	  left: 0px;
	  z-index: 9999999;
	  background-color: rgba(255, 255, 255, 0.85); }

	.pio-loading2 .pio-loading2-box {
	  width: 35px;
	  height: 35px;
	  border-radius: 100%;
	  position: absolute;
	  left: 0;
	  right: 0;
	  top: 0;
	  bottom: 0;
	  margin: auto; }

	.pio-loading2 h6 {
	  font-size: 20px;
	  position: absolute;
	  /* bottom: -25px; */
	  white-space: nowrap;
	  transform: translateX(-50%);
	  left: 50%;
	  cursor: default; }

	.pio-loading2-box,
	.pio-loading2-box > div {
	  position: relative;
	  -webkit-box-sizing: border-box;
	  -moz-box-sizing: border-box;
	  box-sizing: border-box; }

	.pio-loading2-box {
	  display: block;
	  font-size: 0;
	  color: #98bff6; }

	.pio-loading2-box.pio-la-dark {
	  color: #333; }

	.pio-loading2-box > div {
	  display: inline-block;
	  float: none;
	  background-color: currentColor;
	  border: 0 solid currentColor; }

	.pio-loading2-box {
	  width: 32px;
	  height: 32px; }

	.pio-loading2-box > div:nth-child(1),
	.pio-loading2-box > div:nth-child(2) {
	  position: absolute;
	  left: 0;
	  width: 100%; }

	.pio-loading2-box > div:nth-child(1) {
	  top: -25%;
	  z-index: 1;
	  height: 100%;
	  border-radius: 10%;
	  -webkit-animation: square-jelly-box-animate .6s -.1s linear infinite;
	  -moz-animation: square-jelly-box-animate .6s -.1s linear infinite;
	  -o-animation: square-jelly-box-animate .6s -.1s linear infinite;
	  animation: square-jelly-box-animate .6s -.1s linear infinite; }

	.pio-loading2-box > div:nth-child(2) {
	  bottom: -9%;
	  height: 10%;
	  background: #6281af;
	  border-radius: 50%;
	  opacity: .2;
	  -webkit-animation: square-jelly-box-shadow .6s -.1s linear infinite;
	  -moz-animation: square-jelly-box-shadow .6s -.1s linear infinite;
	  -o-animation: square-jelly-box-shadow .6s -.1s linear infinite;
	  animation: square-jelly-box-shadow .6s -.1s linear infinite; }

	@-webkit-keyframes square-jelly-box-animate {
	  17% {
	    border-bottom-right-radius: 10%; }
	  25% {
	    -webkit-transform: translateY(25%) rotate(22.5deg);
	    transform: translateY(25%) rotate(22.5deg); }
	  50% {
	    border-bottom-right-radius: 100%;
	    -webkit-transform: translateY(50%) scale(1, 0.9) rotate(45deg);
	    transform: translateY(50%) scale(1, 0.9) rotate(45deg); }
	  75% {
	    -webkit-transform: translateY(25%) rotate(67.5deg);
	    transform: translateY(25%) rotate(67.5deg); }
	  100% {
	    -webkit-transform: translateY(0) rotate(90deg);
	    transform: translateY(0) rotate(90deg); } }
	@-moz-keyframes square-jelly-box-animate {
	  17% {
	    border-bottom-right-radius: 10%; }
	  25% {
	    -moz-transform: translateY(25%) rotate(22.5deg);
	    transform: translateY(25%) rotate(22.5deg); }
	  50% {
	    border-bottom-right-radius: 100%;
	    -moz-transform: translateY(50%) scale(1, 0.9) rotate(45deg);
	    transform: translateY(50%) scale(1, 0.9) rotate(45deg); }
	  75% {
	    -moz-transform: translateY(25%) rotate(67.5deg);
	    transform: translateY(25%) rotate(67.5deg); }
	  100% {
	    -moz-transform: translateY(0) rotate(90deg);
	    transform: translateY(0) rotate(90deg); } }
	@-o-keyframes square-jelly-box-animate {
	  17% {
	    border-bottom-right-radius: 10%; }
	  25% {
	    -o-transform: translateY(25%) rotate(22.5deg);
	    transform: translateY(25%) rotate(22.5deg); }
	  50% {
	    border-bottom-right-radius: 100%;
	    -o-transform: translateY(50%) scale(1, 0.9) rotate(45deg);
	    transform: translateY(50%) scale(1, 0.9) rotate(45deg); }
	  75% {
	    -o-transform: translateY(25%) rotate(67.5deg);
	    transform: translateY(25%) rotate(67.5deg); }
	  100% {
	    -o-transform: translateY(0) rotate(90deg);
	    transform: translateY(0) rotate(90deg); } }
	@keyframes square-jelly-box-animate {
	  17% {
	    border-bottom-right-radius: 10%; }
	  25% {
	    -webkit-transform: translateY(25%) rotate(22.5deg);
	    -moz-transform: translateY(25%) rotate(22.5deg);
	    -o-transform: translateY(25%) rotate(22.5deg);
	    transform: translateY(25%) rotate(22.5deg); }
	  50% {
	    border-bottom-right-radius: 100%;
	    -webkit-transform: translateY(50%) scale(1, 0.9) rotate(45deg);
	    -moz-transform: translateY(50%) scale(1, 0.9) rotate(45deg);
	    -o-transform: translateY(50%) scale(1, 0.9) rotate(45deg);
	    transform: translateY(50%) scale(1, 0.9) rotate(45deg); }
	  75% {
	    -webkit-transform: translateY(25%) rotate(67.5deg);
	    -moz-transform: translateY(25%) rotate(67.5deg);
	    -o-transform: translateY(25%) rotate(67.5deg);
	    transform: translateY(25%) rotate(67.5deg); }
	  100% {
	    -webkit-transform: translateY(0) rotate(90deg);
	    -moz-transform: translateY(0) rotate(90deg);
	    -o-transform: translateY(0) rotate(90deg);
	    transform: translateY(0) rotate(90deg); } }
	@-webkit-keyframes square-jelly-box-shadow {
	  50% {
	    -webkit-transform: scale(1.25, 1);
	    transform: scale(1.25, 1); } }
	@-moz-keyframes square-jelly-box-shadow {
	  50% {
	    -moz-transform: scale(1.25, 1);
	    transform: scale(1.25, 1); } }
	@-o-keyframes square-jelly-box-shadow {
	  50% {
	    -o-transform: scale(1.25, 1);
	    transform: scale(1.25, 1); } }
	@keyframes square-jelly-box-shadow {
	  50% {
	    -webkit-transform: scale(1.25, 1);
	    -moz-transform: scale(1.25, 1);
	    -o-transform: scale(1.25, 1);
	    transform: scale(1.25, 1); } }
</style>