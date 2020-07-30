import {getFloatingTopOffset} from 'global/ts/utils/offset';


export function initAsideRightPositionFixed() {
    const isAsideRightPresent = document.querySelector('.aside-right');
    if (isAsideRightPresent) {
        fixAsideRightOnScroll();
    }
}


function fixAsideRightOnScroll() {
    const floatingTopOffset = getFloatingTopOffset();
    console.log(floatingTopOffset)
    const asideRightContainer = $('.aside-right');
    const asideRight = asideRightContainer.find('.aside-right-fixed');
    const asideRightContainerOffset = asideRightContainer.offset().top as number;
    const layoutXXL = 1200;
    $(window).on('scroll', function () {
        const isOffsetReached = $(window).scrollTop() > asideRightContainerOffset - floatingTopOffset;
        const isLayoutXXL = window.outerWidth > layoutXXL;
        if (isOffsetReached && isLayoutXXL) {
            asideRight.css('position', 'fixed').css('top', floatingTopOffset);
        } else {
            asideRight.css('position', 'relative');
            asideRight.css('top', 0);
        }
    });
    $(window).on('resize', function() {
        if (window.outerWidth < layoutXXL) {
            asideRight.css('display', 'none');
        } else {
            asideRight.css('display', 'inherit');
        }
    });
}
