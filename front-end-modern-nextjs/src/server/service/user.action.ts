import { OptionType } from "@/types"
import get from "../actions/get.action"
import buildRoute from "../service/route.build"


const userService = {
    'getProfile': async (options: OptionType = {}) => {
        try {
            const data = await get(`${buildRoute('/users/get-user-by-token/')}`, options)
            return data
        }
        catch (error) {
            // console.log(error)
            return null
        }
    }
}

export default userService