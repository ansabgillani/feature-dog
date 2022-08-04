def profile_directory_path(instance, filename):

    # file will be uploaded to MEDIA_ROOT/user_assets/<profile_id>/profile_image/<filename>
    return '{0}/{1}/{2}/{3}'.format('user_assets', instance.pk, 'profile_image', filename)


def logo_directory_path(instance, filename):

    # file will be uploaded to MEDIA_ROOT/organization_assets/<organization_name>/logo/<filename>
    return '{0}/{1}/{2}/{3}'.format('organization_assets', instance.organization_name, 'logo', filename)
