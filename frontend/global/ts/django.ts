export interface DJANGO {
    env: string  // see settings.DJANGO_ENV
    isDebugMode: boolean
}


declare global {
    export interface Window {
        DJANGO: DJANGO;
    }
}
