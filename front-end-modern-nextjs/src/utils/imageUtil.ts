import {
    cplusplusoriginalImg,
    csharporiginalImg,
    pythonoriginalImg,
    javaoriginalImg,
    javascriptoriginalImg,
    typescriptoriginalImg,
} from '@/src/constant/image'


const getImageUtil = (name: string) => {
    name = name.toLowerCase()
    if (name.includes('c++') || name.includes('cpp')) {
        return cplusplusoriginalImg
    }
    if (name.includes('c#')) {
        return csharporiginalImg
    }
    if (name.includes('python')) {
        return pythonoriginalImg
    }
    if (name.includes('java')) {
        return javaoriginalImg
    }
    if (name.includes('javascript')) {
        return javascriptoriginalImg
    }
    return typescriptoriginalImg
}

export default getImageUtil