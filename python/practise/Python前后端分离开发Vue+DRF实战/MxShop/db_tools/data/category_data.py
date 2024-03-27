#!/usr/bin/env python
# encoding: utf-8

row_data = [
    {
        'sub_categorys': [
            {
                'sub_categorys': [
                    {
                        'code': 'yr',
                        'name': '羊肉'
                    },
                    {
                        'code': 'ql',
                        'name': '禽类'
                    },
                    {
                        'code': 'zr',
                        'name': '猪肉'
                    },
                    {
                        'code': 'nr',
                        'name': '牛肉'
                    }
                ],
                'code': 'jprl',
                'name': '精品肉类'
            },
            {
                'sub_categorys': [
                    {
                        'code': 'cb',
                        'name': '参鲍'
                    },
                    {
                        'code': 'yu',
                        'name': '鱼'
                    },
                    {
                        'code': 'xia',
                        'name': '虾'
                    },
                    {
                        'code': 'xb',
                        'name': '蟹/贝'
                    }
                ],
                'code': 'hxsc',
                'name': '海鲜水产'
            },
            {
                'sub_categorys': [
                    {
                        'code': 'xhd_xyd',
                        'name': '松花蛋/咸鸭蛋'
                    },
                    {
                        'code': 'jd',
                        'name': '鸡蛋'
                    }
                ],
                'code': 'dzp',
                'name': '蛋制品'
            },
            {
                'sub_categorys': [
                    {
                        'code': 'sc',
                        'name': '生菜'
                    },
                    {
                        'code': 'bc',
                        'name': '菠菜'
                    },
                    {
                        'code': 'yj',
                        'name': '圆椒'
                    },
                    {
                        'code': 'xlh',
                        'name': '西兰花'
                    }
                ],
                'code': 'ycl',
                'name': '叶菜类'
            },
            {
                'sub_categorys': [

                ],
                'code': 'gjl',
                'name': '根茎类'
            },
            {
                'sub_categorys': [

                ],
                'code': 'qgl',
                'name': '茄果类'
            },
            {
                'sub_categorys': [

                ],
                'code': 'jgl',
                'name': '菌菇类'
            },
            {
                'sub_categorys': [

                ],
                'code': 'jksx',
                'name': '进口生鲜'
            }
        ],
        'code': 'sxsp',
        'name': '生鲜食品'
    },
    {
        'sub_categorys': [
            {
                'sub_categorys': [
                    {
                        'code': 'wly',
                        'name': '五粮液'
                    },
                    {
                        'code': 'lzlj',
                        'name': '泸州老窖'
                    },
                    {
                        'code': 'mt',
                        'name': '茅台'
                    }
                ],
                'code': 'bk',
                'name': '白酒'
            },
            {
                'sub_categorys': [

                ],
                'code': 'ptj',
                'name': '葡萄酒'
            },
            {
                'sub_categorys': [

                ],
                'code': 'yj',
                'name': '洋酒'
            },
            {
                'sub_categorys': [

                ],
                'code': 'pj',
                'name': '啤酒'
            },
            {
                'sub_categorys': [
                    {
                        'code': 'qtpp',
                        'name': '其他品牌'
                    },
                    {
                        'code': 'hj',
                        'name': '黄酒'
                    },
                    {
                        'code': 'ysj',
                        'name': '养生酒'
                    }
                ],
                'code': 'qtjp',
                'name': '其他酒品'
            },
            {
                'sub_categorys': [

                ],
                'code': 'yls',
                'name': '饮料/水'
            },
            {
                'sub_categorys': [
                    {
                        'code': 'bld',
                        'name': '白兰地'
                    },
                    {
                        'code': 'wsj',
                        'name': '威士忌'
                    }
                ],
                'code': 'hj',
                'name': '红酒'
            }
        ],
        'code': 'jsyl',
        'name': '酒水饮料'
    },
    {
        'sub_categorys': [
            {
                'sub_categorys': [
                    {
                        'code': '其他食用油',
                        'name': '其他食用油'
                    },
                    {
                        'code': '菜仔油',
                        'name': '菜仔油'
                    },
                    {
                        'code': '花生油',
                        'name': '花生油'
                    },
                    {
                        'code': '橄榄油',
                        'name': '橄榄油'
                    },
                    {
                        'code': '礼盒',
                        'name': '礼盒'
                    }
                ],
                'code': '食用油',
                'name': '食用油'
            },
            {
                'sub_categorys': [
                    {
                        'code': '面粉/面条',
                        'name': '面粉/面条'
                    },
                    {
                        'code': '大米',
                        'name': '大米'
                    },
                    {
                        'code': '意大利面',
                        'name': '意大利面'
                    }
                ],
                'code': '米面杂粮',
                'name': '米面杂粮'
            },
            {
                'sub_categorys': [
                    {
                        'code': '调味油/汁',
                        'name': '调味油/汁'
                    },
                    {
                        'code': '酱油/醋',
                        'name': '酱油/醋'
                    }
                ],
                'code': '厨房调料',
                'name': '厨房调料'
            },
            {
                'sub_categorys': [

                ],
                'code': '南北干货',
                'name': '南北干货'
            },
            {
                'sub_categorys': [

                ],
                'code': '方便速食',
                'name': '方便速食'
            },
            {
                'sub_categorys': [

                ],
                'code': '调味品',
                'name': '调味品'
            }
        ],
        'code': '粮油副食',
        'name': '粮油副食'
    },
    {
        'sub_categorys': [
            {
                'sub_categorys': [
                    {
                        'code': '西红柿',
                        'name': '西红柿'
                    },
                    {
                        'code': '韭菜',
                        'name': '韭菜'
                    },
                    {
                        'code': '青菜',
                        'name': '青菜'
                    }
                ],
                'code': '有机蔬菜',
                'name': '有机蔬菜'
            },
            {
                'sub_categorys': [
                    {
                        'code': '甘蓝',
                        'name': '甘蓝'
                    },
                    {
                        'code': '胡萝卜',
                        'name': '胡萝卜'
                    },
                    {
                        'code': '黄瓜',
                        'name': '黄瓜'
                    }
                ],
                'code': '精选蔬菜',
                'name': '精选蔬菜'
            },
            {
                'sub_categorys': [
                    {
                        'code': '火龙果',
                        'name': '火龙果'
                    },
                    {
                        'code': '菠萝蜜',
                        'name': '菠萝蜜'
                    },
                    {
                        'code': '奇异果',
                        'name': '奇异果'
                    }
                ],
                'code': '进口水果',
                'name': '进口水果'
            },
            {
                'sub_categorys': [
                    {
                        'code': '水果礼盒',
                        'name': '水果礼盒'
                    },
                    {
                        'code': '苹果',
                        'name': '苹果'
                    },
                    {
                        'code': '雪梨',
                        'name': '雪梨'
                    }
                ],
                'code': '国产水果',
                'name': '国产水果'
            }
        ],
        'code': '蔬菜水果',
        'name': '蔬菜水果'
    },
    {
        'sub_categorys': [
            {
                'sub_categorys': [
                    {
                        'code': '果冻',
                        'name': '果冻'
                    },
                    {
                        'code': '枣类',
                        'name': '枣类'
                    },
                    {
                        'code': '蜜饯',
                        'name': '蜜饯'
                    },
                    {
                        'code': '肉类零食',
                        'name': '肉类零食'
                    },
                    {
                        'code': '坚果炒货',
                        'name': '坚果炒货'
                    }
                ],
                'code': '休闲零食',
                'name': '休闲零食'
            },
            {
                'sub_categorys': [
                    {
                        'code': '创意喜糖',
                        'name': '创意喜糖'
                    },
                    {
                        'code': '口香糖',
                        'name': '口香糖'
                    },
                    {
                        'code': '软糖',
                        'name': '软糖'
                    },
                    {
                        'code': '棒棒糖',
                        'name': '棒棒糖'
                    }
                ],
                'code': '糖果',
                'name': '糖果'
            },
            {
                'sub_categorys': [
                    {
                        'code': '夹心巧克力',
                        'name': '夹心巧克力'
                    },
                    {
                        'code': '白巧克力',
                        'name': '白巧克力'
                    },
                    {
                        'code': '松露巧克力',
                        'name': '松露巧克力'
                    },
                    {
                        'code': '黑巧克力',
                        'name': '黑巧克力'
                    }
                ],
                'code': '巧克力',
                'name': '巧克力'
            },
            {
                'sub_categorys': [
                    {
                        'code': '牛肉干',
                        'name': '牛肉干'
                    },
                    {
                        'code': '猪肉脯',
                        'name': '猪肉脯'
                    },
                    {
                        'code': '牛肉粒',
                        'name': '牛肉粒'
                    },
                    {
                        'code': '猪肉干',
                        'name': '猪肉干'
                    }
                ],
                'code': '肉干肉脯/豆干',
                'name': '肉干肉脯/豆干'
            },
            {
                'sub_categorys': [
                    {
                        'code': '鱿鱼足',
                        'name': '鱿鱼足'
                    },
                    {
                        'code': '鱿鱼丝',
                        'name': '鱿鱼丝'
                    },
                    {
                        'code': '墨鱼/乌贼',
                        'name': '墨鱼/乌贼'
                    },
                    {
                        'code': '鱿鱼仔',
                        'name': '鱿鱼仔'
                    },
                    {
                        'code': '鱿鱼片',
                        'name': '鱿鱼片'
                    }
                ],
                'code': '鱿鱼丝/鱼干',
                'name': '鱿鱼丝/鱼干'
            }
        ],
        'code': '休闲食品',
        'name': '休闲食品'
    },
    {
        'sub_categorys': [
            {
                'sub_categorys': [

                ],
                'code': '进口奶品',
                'name': '进口奶品'
            },
            {
                'sub_categorys': [

                ],
                'code': '国产奶品',
                'name': '国产奶品'
            },
            {
                'sub_categorys': [

                ],
                'code': '奶粉',
                'name': '奶粉'
            },
            {
                'sub_categorys': [

                ],
                'code': '有机奶',
                'name': '有机奶'
            },
            {
                'sub_categorys': [

                ],
                'code': '原料奶',
                'name': '原料奶'
            }
        ],
        'code': '奶类食品',
        'name': '奶类食品'
    },
    {
        'sub_categorys': [
            {
                'sub_categorys': [

                ],
                'code': '菌菇类',
                'name': '菌菇类'
            },
            {
                'sub_categorys': [

                ],
                'code': '腌干海产',
                'name': '腌干海产'
            },
            {
                'sub_categorys': [

                ],
                'code': '汤料',
                'name': '汤料'
            },
            {
                'sub_categorys': [

                ],
                'code': '豆类',
                'name': '豆类'
            },
            {
                'sub_categorys': [

                ],
                'code': '干菜/菜干',
                'name': '干菜/菜干'
            },
            {
                'sub_categorys': [

                ],
                'code': '干果/果干',
                'name': '干果/果干'
            },
            {
                'sub_categorys': [

                ],
                'code': '豆制品',
                'name': '豆制品'
            },
            {
                'sub_categorys': [

                ],
                'code': '腊味',
                'name': '腊味'
            }
        ],
        'code': '天然干货',
        'name': '天然干货'
    },
    {
        'sub_categorys': [
            {
                'sub_categorys': [

                ],
                'code': '白茶',
                'name': '白茶'
            },
            {
                'sub_categorys': [

                ],
                'code': '红茶',
                'name': '红茶'
            },
            {
                'sub_categorys': [

                ],
                'code': '绿茶',
                'name': '绿茶'
            }
        ],
        'code': '精选茗茶',
        'name': '精选茗茶'
    }
]