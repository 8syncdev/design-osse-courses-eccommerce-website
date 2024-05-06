import get from "./actions/get.action";
import post from "./actions/post.action";
import { API_BE_SSR } from "./actions/const";
import courseService from "./service/course.action";

export {
    get,
    post,
    // API Link
    API_BE_SSR,
    // Service
    courseService
}