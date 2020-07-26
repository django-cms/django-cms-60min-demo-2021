export function getFloatingTopOffset(): number { 
    const toolbarHeight = $('.cms-toolbar').height() || 0 as number;
    const navbarHeight = $('header nav').outerHeight() as number;
    const floatingTopOffset = toolbarHeight + navbarHeight;
    return floatingTopOffset;
}
