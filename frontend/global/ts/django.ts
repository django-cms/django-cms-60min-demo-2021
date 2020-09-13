export interface django {
    env: string, // see settings.DJANGO_ENV
    isDebugMode: boolean,
    algoliaApplicationId: string,
    algoliaApiKey: string,
}


declare global {
    export interface Window {
        django: django;
    }
}
