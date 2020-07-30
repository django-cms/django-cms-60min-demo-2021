export function getFloatingTopOffset(): number { 
    const toolbarHeight = $('.cms-toolbar').height() || 0 as number;
    const navbarFixedHeight = $('header nav.fixed-top').outerHeight() || 0 as number;
    const floatingTopOffset = toolbarHeight + navbarFixedHeight;
    return floatingTopOffset;
}
