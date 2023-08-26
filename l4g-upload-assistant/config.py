config = {
    "DEFAULT" : {
    
        # ------ READ THIS ------
        # Any lines starting with the # symbol are commented and will not be used.
        # If you change any of these options, remove the #
        # -----------------------

        "tmdb_api" : "tmdb api key",
        "imgbb_api" : "omgbb api key",
        "ptpimg_api" : "ptpimg api key",
        "lensdump_api" : "lensdump api key",

        # Order of image hosts, and backup image hosts
        "img_host_1": "imgbb",
        "img_host_2": "ptpimg",
        "img_host_3": "imgbox",
	      "img_host_4": "pixhost",
        "img_host_5": "lensdump",


        "screens" : "6",
        # Enable lossless PNG Compression (True/False)
        "optimize_images" : True,


        # The name of your default torrent client, set in the torrent client sections below
        "default_torrent_client" : "qbit_sample",

        # Play the bell sound effect when asking for confirmation
        "sfx_on_prompt" : True,

    },

    "TRACKERS" : {
        # Which trackers do you want to upload to?
        #"default_trackers" : "BLU, BHD, AITHER, STC, STT, SN, THR, R4E, HP, ACM, PTP, LCD, LST, PTER, NBL, ANT, MTV",
        "default_trackers" : "AITHER", # doesn't matter, we use the command anyway

        "BLU" : {
            "useAPI" : True, # Set to True if using BLU
            "api_key" : "api key",
            "announce_url" : "https://blutopia.cc/announce/announceurl",
            # "anon" : False
        },
        "BHD" : {
            "api_key" : "BHD api key",
            "announce_url" : "https://beyond-hd.me/announce/customannounceurl",
            "draft_default" : "True",
            # "anon" : False
        },
        "PTP" : {
            "useAPI" : False, # Set to True if using PTP
            "add_web_source_to_desc" : True,
            "ApiUser" : "ptp api user",
            "ApiKey" : 'ptp api key',
            "username" : "",
            "password" : "",
            "announce_url" : ""
        },
        "AITHER" :{
            "api_key" : "api key",
            "announce_url" : "https://aither.cc/announce/announceurl",
            # "anon" : False
        },
        "R4E" :{
            "api_key" : "R4E api key",
            "announce_url" : "https://racing4everyone.eu/announce/customannounceurl",
            # "anon" : False
        },
        "HUNO" : {
            "api_key" : "HUNO api key",
            "announce_url" : "https://hawke.uno/announce/customannounceurl",
            # "anon" : False
        },
	    "MTV": {
            'api_key' : 'api key',
            'username' : 'Schaka',
            'password' : 'password',
            "announce_url": "http://tracker.morethantv.me:2710/announekey/announce",
            "anon" : False
        },
        "STC" :{
            "api_key" : "STC",
            "announce_url" : "https://skipthecommericals.xyz/announce/customannounceurl",
            # "anon" : False
        },
        "STT" :{
            "api_key" : "STC",
            "announce_url" : "https://stt.xyz/announce/customannounceurl",
            # "anon" : False
        },
        "SN": {
            "api_key": "api key",
            "announce_url": "https://tracker.swarmazon.club:8443/<YOUR_PASSKEY>/announce",
        },
        "HP" :{
            "api_key" : "HP",
            "announce_url" : "https://hidden-palace.net/announce/customannounceurl",
            # "anon" : False
        },
        "ACM" :{
            "api_key" : "ACM api key",
            "announce_url" : "https://asiancinema.me/announce/customannounceurl",
            # "anon" : False,

            # FOR INTERNAL USE ONLY:
            # "internal" : True,
            # "internal_groups" : ["What", "Internal", "Groups", "Are", "You", "In"],
        },
        "NBL" : {
            "api_key" : "NBL api key",
            "announce_url" : "https://nebulance.io/customannounceurl",
        },
        "ANT" :{
            "api_key" : "ANT api key",
            "announce_url" : "https://anthelion.me/announce/customannounceurl",
            # "anon" : False
        },
        "THR" : {
            "username" : "username",
            "password" : "password",
            "img_api" : "get this from the forum post",
            "announce_url" : "http://www.torrenthr.org/announce.php?passkey=yourpasskeyhere",
            "pronfo_api_key" : "pronfo api key",
            "pronfo_theme" : "pronfo theme code",
            "pronfo_rapi_id" : "pronfo remote api id",
            # "anon" : False
        },
        "LCD" : {
            "api_key" : "LCD api key",
            "announce_url" : "https://locadora.cc/announce/customannounceurl",
            # "anon" : False
        },
        "LST" : {
            "api_key" : "LST api key",
            "announce_url" : "https://lst.gg/announce/customannounceurl",
            # "anon" : False
        },
	    "LT" : {
            "api_key" : "LT api key",
            "announce_url" : "https://lat-team.com/announce/customannounceurl",
            # "anon" : False
        },
        "PTER" : {
            "passkey":'passkey',
            "img_rehost" : False,
            "username" : "",
            "password" : "",
            "ptgen_api": "",
            "anon": True,
        },
        "TL": {
            "announce_key": "announce key",
        },
        "TDC" :{
            "api_key" : "TDC api key",
            "announce_url" : "https://thedarkcommunity.cc/announce/customannounceurl",
            # "anon" : "False"
        },
        "HDT" : {
            "username" : "Username",
            "password" : "password",
            "announce_url" : "https://hdts-announce.ru/announce.php",
            # "anon" : "False"
        },

        "MANUAL" : {
            # Uncomment and replace link with filebrowser (https://github.com/filebrowser/filebrowser) link to the Upload-Assistant directory, this will link to your filebrowser instead of uploading to uguu.se
            # "filebrowser" : "https://domain.tld/filebrowser/files/Upload-Assistant/"
        },
    },


    "TORRENT_CLIENTS" : {
        # Name your torrent clients here, for example, this example is named "Client1"
        "qbit_sample" : {
            "torrent_client" : "qbit",
            "enable_search" : True,
            "qbit_url" : "http://GluetunVPN", # this is my docker container on the same network, which qbit sits behind
            "qbit_port" : "8082",
            "qbit_user" : "admin",
            "qbit_pass" : "adminadmin",
            "torrent_storage_dir" : "/BT_backup", # this is mapped in the command above in line 6
            # "qbit_tag" : "tag",
            # "qbit_cat" : "category"
            
            # Content Layout for adding .torrents: "Original"(recommended)/"Subfolder"/"NoSubfolder"
            "content_layout" : "Original",
            
            # Enable automatic torrent management if listed path(s) are present in the path
                # If using remote path mapping, use remote path
                # For using multiple paths, use a list ["path1", "path2"] 
            # "automatic_management_paths" : ""



            # Remote path mapping (docker/etc.) CASE SENSITIVE
            "local_path" : "/downloads", # this is the mapping in L4G
            "remote_path" : "/data" # the qbittorrent container uses /data, so paths for torrents are wrong

            # Set to False to skip verify certificate for HTTPS connections; for instance, if the connection is using a self-signed certificate.
            # "VERIFY_WEBUI_CERTIFICATE" : True
        }
    },







    "DISCORD" :{
        "discord_bot_token" : "discord bot token",
        "discord_bot_description" : "L4G's Upload Assistant",
        "command_prefix" : "!",
        "discord_channel_id" : "discord channel id for use",
        "admin_id" : "your discord user id",

        "search_dir" : "Path/to/downloads/folder/   this is used for search",
        # Alternatively, search multiple folders:
        # "search_dir" : [
        #   "/downloads/dir1",
        #   "/data/dir2",
        # ]
        "discord_emojis" : {
                "BLU": "💙",
                "BHD": "🎉",
                "AITHER": "🛫",
                "STC": "📺",
                "ACM": "🍙",
                "MANUAL" : "📩",
                "UPLOAD" : "✅",
                "CANCEL" : "🚫"
        }
    }
}