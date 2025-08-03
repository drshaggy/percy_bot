from google_drive_downloader import GoogleDriveDownloader as gdd

file_id = '1Z9fTXRb7FlqzgTTXoywgiQP-Z1cH1v3W'
zip_file = '/Users/connor/chess_data/transfer_learning/images/'
show_size = False
gdd.download_file_from_google_drive(file_id=file_id,
                                            dest_path=zip_file,
                                            overwrite=True,
                                            showsize=show_size)