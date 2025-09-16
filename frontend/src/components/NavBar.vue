<script lang="ts">

</script>

<template>
    <nav>
        <RouterLink to="/">메인</RouterLink>
        <RouterLink to="/category">카테고리</RouterLink>
    </nav>
</template>

<style>
    nav {
        width: 100;
        height: 50px;
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 50px;

        a {
            text-decoration: none;
            color: inherit;
            font-size: 18px;
            min-width: 150px;
            text-align: center;

            &:hover {
                text-decoration: underline;
                text-underline-offset: 5px;
            }
        }
    }
</style>