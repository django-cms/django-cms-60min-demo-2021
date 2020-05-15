export interface DJANGO {
    env: string  // see settings.DJANGO_ENV
    isDebugMode: boolean
    algoliaApplicationId: string
    algoliaApiKey: string
}


declare global {
    export interface Window {
        DJANGO: DJANGO;
    }
}
