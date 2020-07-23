<template>
    <ais-pagination
        class="pagination"
        v-bind:show-previous="false"
        v-bind:show-next="false"
        v-bind:padding="3"
        v-if="searchQuery !== ''"
    >
        <template slot-scope="{
            currentRefinement,
            nbPages,
            pages,
            isFirstPage,
            isLastPage,
            refine,
            createURL
        }">
            <div class="asi-Pagination-container" v-if="nbPages > 1">
                <span v-if="!isFirstPage" class="asi-Pagination-item-edge">
                    <a :href="createURL(0)" @click.prevent="refine(0)">‹‹</a>
                </span>
                
                <div class="ais-Pagination-item"  v-for="page in pages" :key="page">
                    <a
                        :href="createURL(page)"
                        :style="{ fontWeight: page === currentRefinement ? 'bold' : '' }"
                        @click.prevent="refine(page)"
                    >
                        {{ page + 1 }}
                        
                    </a>
                </div>

                <span v-if="!isLastPage" class="asi-Pagination-item-edge">
                    <a :href="createURL(nbPages - 1)" @click.prevent="refine(nbPages - 1)">››</a>
                </span>
            </div>
            <div v-else></div>
        </template>
    </ais-pagination>
</template>

<script>
    module.exports = {
        name: 'ea-ais-pagination',
        props: {
            searchQuery: '',
        }
    };
</script>
