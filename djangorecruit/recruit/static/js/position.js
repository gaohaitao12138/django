
$(document).ready(function() {
    // 初始时隐藏所有可展开的内容
    $(".expandable-content").hide();

    // 定义一个函数来收起所有可展开的内容
    function collapseAll() {
        $(".expandable-content").slideUp("slow");
        $(".sq.toggle-button").removeClass("active").hide();
        $(".zk.toggle-button").show();
    }

    // 监听展开详情按钮的点击事件
    $(".zk.toggle-button").click(function() {
        // 首先收起所有内容
        collapseAll();

        // 找到与当前按钮关联的 flex-container
        var $flexContainer = $(this).closest(".flex-container");
        // 找到对应的可展开内容
        var targetId = $flexContainer.data("target");
        var $targetContent = $("#" + targetId);

        // 展开当前内容
        $targetContent.slideDown("slow");
        // 切换按钮的显示状态
        $(this).hide().next(".sq.toggle-button").show().addClass("active");
    });

    // 监听收起详情按钮的点击事件
    $(".sq.toggle-button").click(function() {
        // 切换按钮的显示状态并移除 active 类以恢复默认边框颜色
        $(this).removeClass("active").hide().prev(".zk.toggle-button").show();
        // 找到与当前按钮关联的 flex-container
        var $flexContainer = $(this).closest(".flex-container");
        // 找到对应的可展开内容并隐藏它
        var targetId = $flexContainer.data("target");
        var $targetContent = $("#" + targetId);
        $targetContent.slideUp("slow");
    });
});





