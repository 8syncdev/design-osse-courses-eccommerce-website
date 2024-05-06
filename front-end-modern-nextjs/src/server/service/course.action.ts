import { OptionType } from "@/types"
import get from "../actions/get.action"
import buildRoute from "../service/route.build"


const courseService = {
    'getCourse': async (options: OptionType = {}) => {
        try {
            const data = await get(`${buildRoute('/courses/')}`, options)
            return data
        }
        catch (error) {
            // console.log(error)
            return null
        }
    },
    'getCourseDetail': async (course_id: number, options: OptionType = {}) => {
        try {
            const data = await get(`${buildRoute(`/lessons/${course_id}/list-lesson-of-course/`)}`, options)
            console.log(data)
            return data
        }
        catch (error) {
            // console.log(error)
            return null
        }
    }
}

export default courseService