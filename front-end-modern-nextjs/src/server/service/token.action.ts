import { OptionType } from "@/types"
import get from "../actions/get.action"
import buildRoute from "../service/route.build"
import post from "../actions/post.action"


const tokenService = ({
    'getTokenByEmailOnly': async (body: any) => {
        try {
            const data = await post(buildRoute('/api-view/token/'), body,{}, 'no-cache')
            // console.log(data)
            return data
        }
        catch (error) {
            // console.log(error)
            return null
        }
    },
    'checkTokenValid': async (options: OptionType = {}) => {
        try {
            const data = await get(`${buildRoute('/api-view/token/')}`, options, 'no-cache')
            // console.log(data)
            return data
        }
        catch (error) {
            // console.log(error)
            return null
        }
    }
})

export default tokenService