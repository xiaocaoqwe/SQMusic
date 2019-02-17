$(document).ready(function () {
    $(window).scroll(function () {
        var totalHeight = $(document).height();
        var scrollTop = $(window).scrollTop();
        var seeHeight = $(window).height()
        var a = "<div class='list-warp'><div style='text-align: center'><a href='/singer/detail-"
        var b = "' target='_blank'><img src='/static/images/"
        var c = ".jpg' title='"
        var d = "' width='200' height='200'></a></div><div style='text-align: center'>"
        var e = "</div></div>"
        if (scrollTop + seeHeight + 30 > totalHeight) {
            var start = $(".list-warp").length;
            $.ajax({
                url: window.location.pathname,
                async: false,
                type: "POST",
                dataType: 'JSON',
                data: {start: start},
                success: function (data) {
                    for (var i = 0; i < data.length; i++) {
                        var id = data[i]['pk'];
                        var name = data[i]['fields']['name'];
                        $(".list").append(a + id + b + name + c + name + d + name + e);
                    }
                }
            })
        }
    })
});
