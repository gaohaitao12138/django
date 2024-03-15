$(document).ready(function(){
    $('.slick-carousel').slick({
        slidesToShow: 1, // 同时显示的幻灯片数量
        slidesToScroll: 1, // 每次滑动时滑动的幻灯片数量
        autoplay: true, // 是否自动播放
        autoplaySpeed: 3000, // 自动播放的速度（毫秒）
        arrows: true, // 是否显示箭头
        customPaging: function(slider, i) {
            return '<button type="button">' + (i + 1) + '</button>';
        },
        // 其他设置项...
    });

    // 如果需要，可以自定义箭头或添加额外的事件处理逻辑
    $('.slick-prev').on('click', function() {
        $('.slick-carousel').slick('slickPrev');
    });

    $('.slick-next').on('click', function() {
        $('.slick-carousel').slick('slickNext');
    });

    // 也可以监听其他事件，例如初始化后、滑动后等
    $('.slick-carousel').on('afterChange', function(event, slick, currentSlide){
        console.log('Current slide is: ' + currentSlide);
    });
});