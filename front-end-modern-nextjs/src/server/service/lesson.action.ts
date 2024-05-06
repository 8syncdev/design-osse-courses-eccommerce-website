import { OptionType, ResponseDetailLessonAPIType, ResponseLessonOfCourseAPIType } from "@/types"
import get from "../actions/get.action"
import buildRoute from "../service/route.build"



const lessonService = {
    'getLessonDetail': async (lesson_id: number, options: OptionType = {}): Promise<ResponseDetailLessonAPIType | null>=> {
        try {
            const data = await get(`${buildRoute(`/detail-lessons/${lesson_id}/`)}`, options)
            // console.log(data)
            return data
        }
        catch (error) {
            // console.log(error)
            return null
        }
    },
    'getAllDetailLessonOfLesson': async (lesson_id: number|null=null, options: OptionType = {}, page: number=1): Promise<ResponseLessonOfCourseAPIType>=> {
        if (lesson_id === null)
            return {
                count: 0,
                links: {
                    next: '',
                    previous: ''
                },
                results: []
            }
        try {
            const data = await get(`${buildRoute(`/detail-lessons/${lesson_id}/list-detaillesson-of-lesson/${page != 1 ?`?page=${page}`:''}`)}`, options,)
            // console.log(data)
            return data
        }
        catch (error) {
            // console.log(error)
            return {
                count: 0,
                links: {
                    next: '',
                    previous: ''
                },
                results: []
            }
        }
    }
}

export default lessonService