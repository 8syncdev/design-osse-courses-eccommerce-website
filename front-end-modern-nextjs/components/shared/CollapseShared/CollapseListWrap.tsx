
import { Button } from '@/components/ui/button'
import { ResponseLessonOfCourseAPIType } from '@/types'
import Link from 'next/link'
import React from 'react'



const CollapseListWrap = async ({
  id,
  page
}: {
  apiFunc: Function,
  id: number,
  page: number
}) => {
  

  return (
    <>
      {id} {page}
    </>
  )
}

export default CollapseListWrap