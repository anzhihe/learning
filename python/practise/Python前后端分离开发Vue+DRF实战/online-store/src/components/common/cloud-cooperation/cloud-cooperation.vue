<template>
    <div class="associate-file">
        <Modal v-model="modalShow" title="云协作" @on-ok="ok" @on-cancel="cancel">
            <div class="wrap">
                
            </div>
            
            
        </Modal>

    </div>
</template>
<script>

    export default {
        data () {
            return {
                modalShow: false,
                

            };
        },
        props: {
            value: {
                type: Boolean,
                default: false
            },
            
        },
        created () {
            
        },
        watch: {
            value (val) {
                
                this.modalShow = val;
            }
        },
        computed: {

        },
        methods: {
            
        }
    }
</script>
<style scoped lang='scss'>

</style>

