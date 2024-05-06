// 'use client'
// import {
//     Pagination,
//     PaginationContent,
//     PaginationEllipsis,
//     PaginationItem,
//     PaginationLink,
//     PaginationNext,
//     PaginationPrevious,
// } from "@/components/ui/pagination"
// import next from "next"
// import { list } from "postcss"
// import React, { use, useEffect } from 'react'

// const PaginationShared = ({
//     base_url,
//     list_page,
//     next_page,
//     prev_page,
//     current_page,
//     setData,
//     apiFunction,
//     setCurrentPage
// }: {
//     base_url: string
//     list_page: number[]
//     next_page?: number | null
//     prev_page?: number | null
//     current_page?: number | null
//     setData: Function
//     apiFunction: Function
//     setCurrentPage: Function
// }) => {
//     console.log(list_page)
//     const handleClick = async (page: number) => {
//         const res = await apiFunction(page)
//         // setData(res)
//         setCurrentPage(page)
//     }

//     useEffect(() => {
//         console.log(current_page)
//     }, [current_page])
//     return (
//         <Pagination>
//             <PaginationContent>
//                 {prev_page ?
//                     <>
//                         <PaginationItem>
//                             <PaginationPrevious href={`#`} onClick={()=>handleClick(prev_page)} />
//                         </PaginationItem>
//                     </> :
//                     <>
//                         <PaginationItem>
//                             <PaginationPrevious href="#" />
//                         </PaginationItem>
//                     </>
//                 }
//                 {list_page && list_page.length > 1 ? [...Array.from({ length: list_page.length}, (_, i) => i + 1)]?.splice(0, (list_page.length) % 5).map((item, index)=> {
//                     return <PaginationItem key={index}>
//                         <PaginationLink href="#" onClick={()=>handleClick(item)}>{item}</PaginationLink>
//                     </PaginationItem>
//                 }) : <></>
//                 }
//                 <PaginationItem>
//                     <PaginationEllipsis />
//                 </PaginationItem>
//                 <PaginationItem>
//                     <PaginationNext href="#" />
//                 </PaginationItem>
//             </PaginationContent>
//         </Pagination>

//     )
// }

// export default PaginationShared