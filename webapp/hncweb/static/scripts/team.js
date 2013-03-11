(function(root){
    root.team = function($, carouselRoot, cFlow){
        carouselRoot.carousel("pause");
        var items = cFlow.children()
            , len = items.length
            , supportsTransitions = function() {
                var b = document.body || document.documentElement, s = b.style, p = 'transition', v;
                if(typeof s[p] == 'string') {return true; }
                v = ['Moz', 'Webkit', 'Khtml', 'O', 'ms'],
                    p = p.charAt(0).toUpperCase() + p.substr(1);
                for(var i=0; i<v.length; i++)if(typeof s[v[i] + p] == 'string'){ return true; }
                return false;
            }
            , supportT = supportsTransitions()
            , positionTrans = function(centerItem, lI, rI){
                var pos, transform_vals = "translateX(0px) rotateY(0deg) translateZ(0) scale(1,1)";
                centerItem.css({"transform": transform_vals});
                for(pos=0;pos<lI.length;pos++){
                    transform_vals = "translateX("+(pos*-100)+"px) rotateY(70deg) translateZ(-"+(200+pos)+"px) scale(.8,.8)";
                    items.eq(lI[pos]).css({"transform": transform_vals, zIndex:2});
                }
                for(pos=0;pos<rI.length;pos++){
                    transform_vals = "translateX("+(pos*100)+"px) rotateY(-70deg) translateZ(-"+(200+pos)+"px) scale(.8,.8)";
                    items.eq(rI[pos]).css({"transform": transform_vals, zIndex:2});
                }
            }
            , positionFix = function(centerItem, lI, rI){
                var pos, middle = $(".team-wrapper").width() / 2;
                centerItem.css({zIndex:len+1})
                    .animate({left:"500px"})
                    .find("img").css({opacity: 1});
                for(pos=0;pos<lI.length;pos++){
                    if(pos+1==lI.length)items.eq(lI[pos]).css({zIndex:0});
                    items.eq(lI[pos])
                        .css({zIndex:len-pos})
                        .animate({left:(400-100*pos)+"px"})
                        .find("img").css({opacity:.9-pos/len});
                }
                for(pos=0;pos<rI.length;pos++){
                    if(pos+1==rI.length)items.eq(rI[pos]).css({zIndex:0});
                    items.eq(rI[pos])
                        .css({zIndex:len-pos})
                        .animate({left:(600+100*pos)+"px"})
                        .find("img").css({opacity:.9-pos/len});
                }
            }
            , transformCovers = function (idx) {
                var centerItem = items.eq(idx), lI = [], rI = [], pos, transform_vals;
                for(pos=1;pos<Math.ceil(len/2);pos++){lI.push((idx-pos + len)%len)}
                for(pos=1;pos<=Math.ceil(len/2);pos++){rI.push((idx+pos + len)%len)}
                if(!centerItem.hasClass('selected')){
                    (supportT?positionTrans:positionFix)(centerItem, lI, rI);
                    centerItem.addClass('selected').siblings('.selected').removeClass('selected');
                }
            };

        transformCovers(Math.ceil(len/2));
        cFlow.on('click','.flowItem:not(.selected)',function(){
            var idx = parseInt($(this).data("slide"), 10), cur = items.filter(".selected").idx;
            transformCovers(idx);
            if(Math.abs(cur - idx) == 1){
                if(cur < idx)carouselRoot.carousel('next');
                else carouselRoot.carousel('prev');
            } else
                carouselRoot.carousel(idx);
        });
        carouselRoot.on({slide: function(e){
            transformCovers($(e.relatedTarget).index());
        }});
    }
})(window);
