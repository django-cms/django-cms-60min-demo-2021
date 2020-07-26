export function initAsideRightPositionFixed() {
    const isMenuPresent = document.querySelectorAll('.metismenu-root');
    if (isMenuPresent) {
        fixLeftMenuOnScroll();
    }
}


function fixLeftMenuOnScroll() {
    const toolbarHeight = $('.cms-toolbar').height() || 0 as number;
    const navbarHeight = $('header nav').outerHeight() as number;
    const floatingTopOffset = toolbarHeight + navbarHeight;
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
