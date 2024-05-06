'use client'
import lessonService from '@/src/server/service/lesson.action'
import React, { memo, useEffect, useState } from 'react'
import Link from 'next/link'
import { ResponseLessonOfCourseAPIType } from '@/types'
import { Button } from '@/components/ui/button'
import LoadingBar from '@/components/comp_dev/LoadingStateDEV/LoadingBar'




const CollapseItemShared = ({ id }: {
    id: number
}) => {
    const [isLoading, setIsLoading] = useState<boolean>(false)
    const [current, setCurrent] = useState<number>(1)
    const [data, setData] = useState<ResponseLessonOfCourseAPIType>({
        count: 0,
        links: {
            next: '',
            previous: ''
        },
        results: []
    })
    const [results, setResults] = useState<{
        page: number,
        data: any[]
    }[]>([])

    useEffect(() => {
        const fetchData = async () => {
            if (id === null) return
            if (results.some(item => item.page === current) === false) {
                setIsLoading(true)
            }
            let res: ResponseLessonOfCourseAPIType = {
                count: 0,
                links: {
                    next: '',
                    previous: ''
                },
                results: []
            }
            /**
             * * Optimize fetching data, when data is already fetched, don't fetch it again, using results.some() to check if the page is already fetched
             */
            if (data.results.length == 0 || results.some(item => item.page === current) === false) {
                res = await lessonService.getAllDetailLessonOfLesson(id, {}, current)
                if (res && res.count > 0) {
                    setData(res)
                }
                else {
                    return
                }
                // * If the page is not fetched, add it to the results
                //* Notice: using res to store the fetched data, then set it to the results, because the state is not updated immediately due to run top to bottom of usestate.
                if (results.some(item => item.page === current) === false) {
                    setResults([...results, { page: current, data: res.results }])
                }
            }
            else {
                const findPage = results.find(item => item.page === current)
                if (findPage) {
                    setData({
                        count: data.count,
                        links: data.links,
                        results: findPage.data
                    })
                }
            }
        }
        // setIsLoading(false)

        fetchData()
    }, [current])

    useEffect(() => {
        // console.log(results)
        if (results.some(item => item.page === current) === true) {
            // console.log(data)
            setIsLoading(false)
        }
    }, [results])

    return (
        <>
            {!isLoading ? data && data.results?.map((item, _index: number) => {
                return <div key={_index} className='flex gap-4 justify-between py-4 border-b-2 rounded-lg mb-1'>
                    <p>{item.name.length > 40 ? `${item.name.slice(0, 40)}...` : item.name}</p>
                    <Link href={{
                        pathname: `/course/lesson/${item?.slug}`,
                        query: { id: item.id },
                    }}>
                        Xem chi tiết
                    </Link>
                </div>
            }) :
                <>
                    <LoadingBar />
                </>
            }

            <div className='py-3 flex justify-center'>
                <div className='flex gap-3'>
                    <Button onClick={() => setCurrent(current => (
                        current > 1 ? current - 1 : current
                    ))}>
                        Quay Lại
                    </Button>

                    <Button onClick={() => setCurrent(current => (
                        current <= Math.ceil(data.count / 10) ? current + 1 : current
                    ))}>
                        Xem Tiếp
                    </Button>
                </div>
            </div>


        </>
    )
}

export default memo(CollapseItemShared)