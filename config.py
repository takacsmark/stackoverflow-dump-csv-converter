config = {
    "PostLinks": {
        "header_line": ["Id", "CreationDate", "PostId", "RelatedPostId", "LinkTypeId"]
    },
    "Posts": {
        "header_line": [
            "Id",
            "PostTypeId",
            "AcceptedAnswerId",
            "CreationDate",
            "Score",
            "ViewCount",
            # "Body",
            "OwnerUserId",
            # "LastEditorUserId",
            # "LastEditorDisplayName",
            # "LastEditDate",
            "LastActivityDate",
            # "Title",
            "Tags",
            "AnswerCount",
            "CommentCount",
            "FavoriteCount",
            "CommunityOwnedDate"
        ]#,
    #     "fixes": {
            # "Title": ['"', '""']
    #     }
    },
    "Tags": {
        "header_line": [
            "Id", 
            "TagName", 
            "Count", 
            "ExcerptPostId", 
            "WikiPostId",
        ]
    },
    "Users": {
        "header_line": [
            "Id",
            "Reputation",
            "CreationDate",
            "DisplayName",
            "LastAccessDate",
            # "WebsiteUrl",
            "Location",
            # "AboutMe",
            "Views",
            "UpVotes",
            "DownVotes",
            # "ProfileImageUrl",
            # "AccountId"
        ],
        "fixes": {
            "Location": ['"', '""']
        }
    }
}

