
STORAGES = {  # django 4.2 and above
    "default": {  # default
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {  # default
        "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
    },
    "cloudflare_images": {  # add
        "BACKEND": "cloudflare_images.django.ImageStorageCloudflare",
    },
}