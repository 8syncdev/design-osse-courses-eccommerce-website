

export type OptionType = {
    'Authorization'?: string
}


/**
 * * Route Literal
 */
export type ROUTE_LITERAL_TYPE = '/courses/' | '/lessons/' | '/detail-lessons/' | '/users/' | 'api-view/token/' | string


/**
 * * Cache API
 */

export type CacheType = RequestCache

/**
 * * Type Form
 */

import { FormLoginSchemaType } from "@/components/shared/FormShared/type"

export type FormLoginType = FormLoginSchemaType

/**
 * * Type API Response
 */

import { ResponseLessonOfCourseType } from "./response"

export type ResponseLessonOfCourseAPIType = ResponseLessonOfCourseType

export type ResponseCoursesAPIType = {
    id: number;
    title: string;
    description: string;
    price: number;
    instructor_name: string;
    extent_name: string;
    created_at: string;
    updated_at: string;
    slug: string;
};

export type ResponseDetailLessonAPIType = {
    id: number;
    name: string;
    extent_name: string;
    created_at: string;
    updated_at: string;
    content: string;
};