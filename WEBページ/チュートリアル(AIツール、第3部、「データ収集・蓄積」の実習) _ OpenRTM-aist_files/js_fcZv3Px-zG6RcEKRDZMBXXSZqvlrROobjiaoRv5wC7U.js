(function($) {
  // アンカーリンクに飛ぶ際のヘッダ高さ分の調整
  $(function() {
    $('a[href^=#]').click(function() {
      var speed = 400;
　　var windowWidth = $(window).width();
      var href= $(this).attr("href");
      var target = $(href == "#" || href == "" ? 'html' : href);
      var headerHeight = $('.header-section-1').height(); //ヘッダーの高さ
      var adj = 0;
　　//以下はログイン時の設定（ログイン時＝-50・ログアウト時＝-30位？)
      if (windowWidth <= 995) {    //ヘッダー 2行　
     　　  adj =  - 50; 
      } else if (windowWidth <= 1250) { //ヘッダー 2行  固定
             adj =  - headerHeight - 50;　  //ターゲットの座標からヘッダの高さ分引く
      } else {　　　　　　　　　　　　     //最大　ヘッダー 1行 固定
             adj =  - headerHeight - 10;  　//ターゲットの座標からヘッダの高さ分引く
      }
      var position = target.offset().top +  adj;
      $('body,html').animate({scrollTop:position}, speed, 'swing');
      console.log($('.stickup').css("position"));
//      console.log('HOGEHOGE2');
      return false;
    });
  });
  $(function() {

    // vspace, hspace.
    $('img').each(function() {
      if ($(this).attr('vspace')) {
        $(this).css('margin-top', $(this).attr('vspace') + 'px');
        $(this).css('margin-bottom', $(this).attr('vspace') + 'px');
      }
      if ($(this).attr('hspace')) {
        $(this).css('margin-left', $(this).attr('hspace') + 'px');
        $(this).css('margin-right', $(this).attr('hspace') + 'px');
      }
    });
    console.log('HOGEHOGE');

    //#3923 +
    /*---------
    function openrtm_node_link_button_auto_move() {
      for (var i = 0; i < 2; i++) {
        var max = 0;
        for (var j = 0; j < 3; j++) {
          var height = parseInt($('.view-mews-new .view-content .grid-4.views-row:nth-child(' + ((i * 2) + j + 1) + ')').innerHeight());
console.log(height);
          if (max < height) {
            max = height;
          }
        }
        for (var j = 0; j < 3; j++) {
          var box = parseInt($('.view-mews-new .view-content .grid-4.views-row:nth-child(' + ((i * 2) + j + 1) + ')').innerHeight());
          var footer = parseInt($('.view-mews-new .view-content .grid-4.views-row:nth-child(' + ((i * 2) + j + 1) + ') .group-footer').innerHeight());
          $('.view-mews-new .grid-4.views-row:nth-child(' + ((i * 2) + j + 1) + ') .group-footer').innerHeight((footer + max - box) + 'px');
        }
      }
    }
    openrtm_node_link_button_auto_move();
    $(window).resize(function() { openrtm_node_link_button_auto_move(); });
    ---*/

    //#3924 +
    /*-------------------------
    function openrtm_quick_start_button_font_size() {
      var minSize = 12;
      var blockSize = parseInt($('#mini-panel-openrtm_starting').innerWidth());
      var fontSize = blockSize / 28;
      if (fontSize < minSize) {
        fontSize = minSize;
      }
      $('#mini-panel-openrtm_starting a').css('font-size', fontSize + 'px');
    }
    openrtm_quick_start_button_font_size();
    $(window).resize(function() { openrtm_quick_start_button_font_size(); });
    -------------*/

    // toc.
    // $('.field-item > table > tbody > tr > td > div#toc').addClass('toc_list');

  });
}) (jQuery);

;
(function($) {
  $(function() {
    var n = 2;
    $('#block-superfish-' + n).removeClass('block-superfish-' + n).addClass('block-superfish-1');
    $('#block-superfish-' + n).attr('id', 'block-superfish-1');
    $('#superfish-' + n).attr('id', 'superfish-1');
  });
}) (jQuery);
;
