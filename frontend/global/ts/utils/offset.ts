export function getFloatingTopOffset(): number { 
    const cmsToolbar = document.querySelector('.cms-toolbar');
    let cmsToolbarHeight = 0;
    if (cmsToolbar) {
        cmsToolbarHeight = 46;
    }

    let navbarFixedHeight = 0;
    const navbarFixed = document.querySelector('header nav.fixed-top');
    if (navbarFixed) {
        navbarFixedHeight = 56;
    }
    const floatingTopOffset = cmsToolbarHeight + navbarFixedHeight;
    return floatingTopOffset;
}
