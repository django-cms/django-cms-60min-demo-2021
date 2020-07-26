import {getFloatingTopOffset} from 'global/ts/utils/offset';

export function initAsideRightPositionFixed() {
    const isAsideRightPresent = document.querySelectorAll('.one-column-with-menu-and-sidebar .aside-right');
    if (isAsideRightPresent) {
        fixAsideRightOnScroll();
    }
}


function fixAsideRightOnScroll() {
    const floatingTopOffset = getFloatingTopOffset();
    const asideRightContainer = $('.aside-right');
    const asideRight = asideRightContainer.find('.aside-right-fixed')
    const asideRightContainerOffset = asideRightContainer.offset().top as number;
    $(window).scroll(function () {
        if ($(window).scrollTop() > asideRightContainerOffset - floatingTopOffset) {
            asideRight.css('position', 'fixed').css('top', floatingTopOffset);
        } else {
            asideRight.css('position', 'relative');
            asideRight.css('top', 0);
        }
    });
}
