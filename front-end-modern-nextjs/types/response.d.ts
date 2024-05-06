export type DetailLessonType = {
    id: number;
    name: string;
    extent_name: string;
    updated_at: string;
    slug: string;
}


export type CourseType = {
    id: number;
    name: string;
    extent_name: string;
    updated_at: string;
    slug?: string;
}

export type ResponseLessonOfCourseType = {
    links: {
        next: string | null;
        previous: string | null;
    };
    count: number;
    results: CourseType[];
}
