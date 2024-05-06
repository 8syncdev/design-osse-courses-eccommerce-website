import React from 'react'
import AuthenTokenProvider from "@/src/provider/AuthenTokenProvider";
import LessonDetailCourse from '@/components/comp_dev/Section/Content/Detail/LessonDetailCourse';

const LessonDetail = ({ params, searchParams }: {
  params: { slug: string },
  searchParams: any
}) => {
  return (
    <AuthenTokenProvider params={params} searchParams={searchParams}>
      <LessonDetailCourse lesson_id={Number(searchParams?.id || 1)} />
    </AuthenTokenProvider>
  )
}

export default LessonDetail