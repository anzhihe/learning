// 使用 Mock
var Mock = require('mockjs');

var login = require('./mock/login.js');
var newOpro = require('./mock/newOpro.js');
var indexList = require('./mock/seriesList.js');
var banners = require('./mock/banner.js');
var menu = require('./mock/menu.js');
var hotSearch = require('./mock/hotSearch.js');

Mock.mock('/login',login)//登录
Mock.mock('/getOpro',newOpro)//首页新品
Mock.mock('/getIndexList',indexList)//首页list
Mock.mock('/getBanner',banners)//首页banner
Mock.mock('/getMenu',menu)//首页menu
Mock.mock('/getHotSearch',hotSearch)//首页热搜

Mock.mock('/product/details', // 商品详情数据
    {
        id: 'sddfsdf', //商品id
        title: '新鲜水果甜蜜香脆单果约800克',
        desc: '食用百香果可以增加胃部饱腹感，减少余热量的摄入，还可以吸附胆固醇和胆汁之类有机分子，抑制人体对脂肪的吸收。因此，长期食用有利于改善人体营养吸收结构，降低体内脂肪，塑造健康优美体态。',
        marketPrice: '232',
        salePrice: '156',
        salesCount: 1000,
        freeFreight: true, //是否免运费
        purNum: 1, //默认购买数量
        detailImages: [
            {
                desc: '第一张细节图',
                src: './images/1(1).jpg',
            },
            {
                desc: '第二张细节图',
                src: './images/1(1).jpg',
            },
            {
                desc: '第三张细节图',
                src: './images/1(1).jpg',
            },
            {
                desc: '第四张细节图',
                src: './images/1(1).jpg',
            }
        ],
        images: [
            {
                desc: '第一张图片的描述',
                src: './images/1(1).jpg',
            },
            {
                desc: '第二张图片的描述',
                src: './images/2.jpg',
            },
            {
                desc: '第三张图片的描述',
                src: './images/3.jpg',
            }
        ]
    }
)
Mock.mock('/product/addShoppingCart', // 某个商品加入购物车
    {

    }
)
Mock.mock('/product/addCollect', // 某个商品加入收藏夹
    {

    }
)
Mock.mock('/hotProduct', // 某个商品加入收藏夹
    [
        {
            img: '',
            title: '1元支付测试商品',
            price: '4'
        },
        {
            img: '',
            title: '1元支付测试商品',
            price: '4'
        },
        {
            img: '',
            title: '1元支付测试商品',
            price: '4'
        },
        {
            img: '',
            title: '1元支付测试商品',
            price: '4'
        },
    ]
)
Mock.mock('/getReceiveInfo', // 收件人信息
    [
        {
            id: '1233',
            province: '北京市', //省
            city: '北京市', // 市
            area: '', // 区
            receiveName: '姓名', // 收件人姓名
            addr: '', // 详细地址
        },
        {
            id: '345',
            province: '四川省', //省
            city: '成都市', // 市
            area: '新都区', // 区
            receiveName: '1254', // 收件人姓名
            addr: '454896', // 详细地址
        }
    ]
)


Mock.mock('/addReceiveInfo', // 添加收获人信息
    {}
)
Mock.mock('/deleteReceiveInfo', // 删除收获人信息
    {}
)

Mock.mock('/getUserInfo', // 获取用户信息
    {
        birthday: '', //格式是xxxx-xx-xx
        sex: '',
        email: '',
        phone: '',
    }
)
Mock.mock('/modifyUserInfo', // 修改用户信息
    {}
)
Mock.mock('/getCollectionList', // 获取收藏列表
    [
        {
            id: '3243', // 商品ID
            title: '田然牛肉大黄瓜条生鲜牛肉冷冻真空黄牛', // 商品名称
            price: 24 //价格
        },
        {
            id: 'dsfsd', // 商品ID
            title: '新鲜水果甜蜜香脆单果约800克', // 商品名称
            price: 24 //价格
        },
        {
            id: 'fsdfg', // 商品ID
            title: '田然牛肉大黄瓜条生鲜牛肉冷冻真空黄牛', // 商品名称
            price: 24 //价格
        },
    ]
)
Mock.mock('/deleteCollect', // 从收藏夹删除商品
    {}
)
Mock.mock('/addConcern', // 加入关注
    {}
)

Mock.mock('/getOrders', // 获取所有订单
    [
        {
            orderId: 122324, //订单号
            time: '2017-07-07 13:48:53', //下单时间
            totalPrice: '123', //订单总金额
            state: '未付款',
        },
        {
            orderId: 122324, //订单号
            time: '2017-07-07 13:48:53', //下单时间
            totalPrice: '123', //订单总金额
            state: '未付款',
        },
    ]
)

Mock.mock('/cancelOrder', // 取消订单
    {}
)
Mock.mock('/product/list', // 商品列表
    {
        listData: [
            {
                id: 'dsafsdf',
                imgurl: 'http://sx.youxueshop.com/images/201512/thumb_img/2_thumb_G_1448945810147.jpg',
                productname: '新鲜水果甜蜜香脆单果约800克',
                description: '食用百香果可以增加胃部饱腹感，减少余热量的摄入，还可以吸附胆固醇和胆汁之类有机分子，抑制人体对脂肪的吸收。因此，长期食用有利于改善人体营养吸收结构，降低体内脂肪，塑造健康优美体态。',
                price: '￥156元',
                sales: 1000
            },
            {
                id: 'q334',
                imgurl: 'http://sx.youxueshop.com/images/201512/thumb_img/7_thumb_G_1448945104346.jpg',
                productname: '潮香村澳洲进口牛排家庭团购套餐20片',
                description: '食用百香果可以增加胃部饱腹感，减少余热量的摄入，还可以吸附胆固醇和胆汁之类有机分子，抑制人体对脂肪的吸收。因此，长期食用有利于改善人体营养吸收结构，降低体内脂肪，塑造健康优美体态。',
                price: '￥232元',
                sales: 1000
            },
            {
                id: '53264',
                imgurl: 'http://sx.youxueshop.com/images/201512/thumb_img/47_thumb_G_1448946213633.jpg',
                productname: '爱食派内蒙古呼伦贝尔冷冻生鲜牛腱子肉1000g',
                description: '食用百香果可以增加胃部饱腹感，减少余热量的摄入，还可以吸附胆固醇和胆汁之类有机分子，抑制人体对脂肪的吸收。因此，长期食用有利于改善人体营养吸收结构，降低体内脂肪，塑造健康优美体态。',
                price: '￥232元',
                sales: 1000
            },
            {
                id: '23425436',
                imgurl: 'http://sx.youxueshop.com/images/201512/thumb_img/4_thumb_G_1448945381841.jpg',
                productname: '澳洲进口牛尾巴300g 新鲜肥牛肉',
                description: '新鲜羊羔肉整只共15斤，原生态大山放牧羊羔，曾经的皇室贡品，央视推荐，2005年北京招待全球财金首脑。五层专用包装箱+真空包装+冰袋+保鲜箱+顺丰冷链发货，路途保质期8天',
                price: '￥232元',
                sales: 300
            },
            {
                id: '4353654',
                imgurl: 'http://sx.youxueshop.com/images/201512/thumb_img/4_thumb_G_1448945381841.jpg',
                productname: '新鲜水果甜蜜香脆单果约800克',
                description: '新鲜羊羔肉整只共15斤，原生态大山放牧羊羔，曾经的皇室贡品，央视推荐，2005年北京招待全球财金首脑。五层专用包装箱+真空包装+冰袋+保鲜箱+顺丰冷链发货，路途保质期8天',
                price: '￥232元',
                sales: 400
            },
            {
                id: '34645643',
                imgurl: 'http://sx.youxueshop.com/images/201512/thumb_img/4_thumb_G_1448945381841.jpg',
                productname: '田然牛肉大黄瓜条生鲜牛肉冷冻真空黄牛',
                description: '前腿+后腿+羊排共8斤，原生态大山放牧羊羔，曾经的皇室贡品，央视推荐，2005年北京招待全球财金首脑。五层专用包装箱+真空包装+冰袋+保鲜箱+顺丰冷链发货，路途保质期8天',
                price: '￥232元',
                sales: 1
            },
            {
                id: '23536',
                imgurl: 'http://sx.youxueshop.com/images/201512/thumb_img/4_thumb_G_1448945381841.jpg',
                productname: '新鲜水果甜蜜香脆单果约800克',
                description: '食用百香果可以增加胃部饱腹感，减少余热量的摄入，还可以吸附胆固醇和胆汁之类有机分子，抑制人体对脂肪的吸收。因此，长期食用有利于改善人体营养吸收结构，降低体内脂肪，塑造健康优美体态。',
                price: '￥232元',
                sales: 2
            },
            {
              id: '23425436',
              imgurl: 'http://sx.youxueshop.com/images/201512/thumb_img/47_thumb_G_1448946213633.jpg',
              productname: '澳洲进口牛尾巴300g 新鲜肥牛肉',
              description: '新鲜羊羔肉整只共15斤，原生态大山放牧羊羔，曾经的皇室贡品，央视推荐，2005年北京招待全球财金首脑。五层专用包装箱+真空包装+冰袋+保鲜箱+顺丰冷链发货，路途保质期8天',
              price: '￥232元',
              sales: 300
            },
        ],
        totalNum: 12
    }

)
Mock.mock('/category', // 菜单列表
    {
        id: 1232434,
        name: '肉类',
        children:[
            {
                id: 123,
                name: '精品肉类',
                children: [
                    {
                        id: 111,
                        name: '羊肉'
                    },
                    {
                        id: 111,
                        name: '牛肉'
                    },
                    {
                        id: 111,
                        name: '猪肉'
                    },
                    {
                        id: 111,
                        name: '鸡肉'
                    },

                ]
            },
            {
                id: 123,
                name: '海鲜水产',
                children: [
                    {
                        id: 111,
                        name: '鱼'
                    },
                    {
                        id: 111,
                        name: '虾'
                    }
                ]
            },
            {
                id: 123,
                name: '精品肉类',
                children: [
                    {
                        id: 111,
                        name: '羊肉'
                    },
                    {
                        id: 111,
                        name: '牛肉'
                    },
                    {
                        id: 111,
                        name: '猪肉'
                    },
                    {
                        id: 111,
                        name: '鸡肉'
                    },

                ]
            },
            {
                id: 123,
                name: '叶菜类',
                children: [
                    {
                        id: 111,
                        name: '生菜'
                    },
                    {
                        id: 111,
                        name: '菠菜'
                    },
                    {
                        id: 111,
                        name: '圆椒'
                    },
                    {
                        id: 111,
                        name: '西兰花'
                    },

                ]
            },
            {
                id: 123,
                name: '叶菜类'
            },
        ]
    }

)
Mock.mock('/currentLoc',
    [
        {
            id: 1,
            name: '首页',
        },
        {
            id: 232,
            name: '酒水饮料',
        },
        {
            id: 456,
            name: '粮油副食',
        },
        {
          id: 56,
          name: '休闲食品',
        },
        {
          id: 6,
          name: '蔬菜水果',
        },
        {
          id: 7,
          name: '奶类食品',
        }


    ]
)
Mock.mock('/priceRange',
    [
        {
            min: 1,
            max: 24,
        },
        {
            min: 15,
            max: 20,
        },
        {
            min: 40,
            max: 80,
        },
        {
            min: 76,
            max: 100,
        },

    ]
)
Mock.mock('/shoppingCartList',  // 请求购物车列表数据
    {
        totalPrice:369,
        goods_list:[{
            id: '23243453',
            image: 'http://sx.youxueshop.com/images/201512/thumb_img/1_thumb_G_1449024889033.jpg',
            title: '新鲜水果甜蜜香脆单果约800克',
            num: 1,
            price: 123,
            total:123
        },
        {
            id: '23243453',
            image:'http://sx.youxueshop.com/images/201512/thumb_img/1_thumb_G_1449024889033.jpg',
            title: '新鲜水果甜蜜香脆单果约800克',
            num: 2,
            price: 123,
            total:123
        },
        {
            id: '23243453',
            image:'http://sx.youxueshop.com/images/201512/thumb_img/1_thumb_G_1449024889033.jpg',
            title: '新鲜水果甜蜜香脆单果约800克',
            num: 4,
            price: 123,
            total:123
        }]

    }

)
Mock.mock('/shoppingCart/addNum',  //购物车数量加一
{

})
Mock.mock('/shoppingCart/reduceNum',  //购物车数量减一
{

})
Mock.mock('/shoppingCart/remove',  //移除购物车某个商品
{

})
Mock.mock('/shoppingCart/clear',  //清空购物车
{

})
Mock.mock('/order/orderInfo',  //获取订单收货人信息
{
    orderStatus: '已完成',
    payStatus: '未付款',
    deliveryStatus: '未发货'
})

Mock.mock('/order/receiveInfo',  //获取订单收货人信息
{
    name: 'dsdsd',
    email: '5655@qq.com',
    post: 934023,
    addr: '地址',
    tel: 2346723,
    mobile: 13834442233,
    symbol: '大厦',
    deliveryTime: '8点'
})
Mock.mock('/order/updateReceiveInfo',  //更新收货人信息
{
    
})
Mock.mock('/message/getAll',  //删除留言
    [
        {
            id: 1234,
            message_type: 1,
            theme: '留言主题',
            message: '留言内容',
            time: '2017-07-19 21:20:25',
        },
        {
            id: 5678,
            message_type: 2,
            theme: '留言主题',
            message: '留言内容',
            time: '2017-07-19 21:20:25',
        }
    ])

Mock.mock('/message/deleteMessage',  //删除留言
{
    
})
Mock.mock('/message/downloadMessage',  //下载上传的文件
{
    
})
Mock.mock('/message/addMessage',  //添加留言
{
    
})
Mock.mock('/address',  //获得所有配送地址
[
    {
        id: '222',
        addr: '成都高新区',
        tel: 18311220453,
        name: 'bobby',
        note: '发顺丰'
    },
    {
        id: '333',
        addr: '成都高新区某小区',
        tel: 18311220453,
        name: 'bobby',
        note: '发顺丰'
    }
])











