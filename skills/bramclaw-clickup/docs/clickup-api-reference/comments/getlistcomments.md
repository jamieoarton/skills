# Get List Comments

View the comments added to a List. \
 \
If you do not include the `start` and `start_id` parameters, this endpoint will return the most recent 25 comments.\
 \
Use the `start` and `start id` parameters of the oldest comment to retrieve the next 25 comments.

# OpenAPI definition

```json
{
  "openapi": "3.1.0",
  "info": {
    "title": "ClickUp API v2 Reference",
    "description": "The ClickUp API enables you to programmatically access and manage your ClickUp resources.\n\n## Authentication\nThe API supports two authentication methods:\n- **Personal API Token**: Use for testing and personal integrations. Add token to requests with header: `Authorization: pk_...`\n- **OAuth 2.0**: Required for building apps for other users. Uses authorization code flow.\n\n## Getting Started\nOur [Getting Started Guide](https://developer.clickup.com/docs/index) provides a comprehensive overview of how to use the ClickUp API.\n",
    "contact": {},
    "version": "2.0"
  },
  "jsonSchemaDialect": "https://json-schema.org/draft/2020-12/schema",
  "servers": [
    {
      "url": "https://api.clickup.com/api",
      "description": "ClickUp",
      "variables": {}
    }
  ],
  "paths": {
    "/v2/list/{list_id}/comment": {
      "get": {
        "summary": "Get List Comments",
        "description": "View the comments added to a List. \\\n \\\nIf you do not include the `start` and `start_id` parameters, this endpoint will return the most recent 25 comments.\\\n \\\nUse the `start` and `start id` parameters of the oldest comment to retrieve the next 25 comments.",
        "tags": [
          "Comments"
        ],
        "operationId": "GetListComments",
        "parameters": [
          {
            "name": "list_id",
            "in": "path",
            "description": "",
            "required": true,
            "style": "simple",
            "schema": {
              "type": "number",
              "contentEncoding": "double",
              "examples": [
                124
              ]
            }
          },
          {
            "name": "start",
            "in": "query",
            "description": "Enter the `date` of a List info comment using Unix time in milliseconds.",
            "style": "form",
            "explode": true,
            "schema": {
              "type": "integer",
              "contentEncoding": "int32"
            }
          },
          {
            "name": "start_id",
            "in": "query",
            "description": "Enter the Comment `id` of a List info comment.",
            "style": "form",
            "explode": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "",
            "headers": {},
            "content": {
              "application/json": {
                "schema": {
                  "title": "GetListCommentsresponse",
                  "required": [
                    "comments"
                  ],
                  "type": "object",
                  "properties": {
                    "comments": {
                      "type": "array",
                      "items": {
                        "$ref": "#/paths/~1v2~1task~1%7Btask_id%7D~1comment/get/responses/200/content/application~1json/schema/properties/comments/items"
                      },
                      "description": ""
                    }
                  },
                  "examples": [
                    {
                      "comments": [
                        {
                          "id": "462",
                          "comment": [
                            {
                              "text": "List comment content"
                            }
                          ],
                          "comment_text": "List comment content",
                          "user": {
                            "id": 183,
                            "username": "John Doe",
                            "initials": "JD",
                            "email": "johndoe@gmail.com",
                            "color": "#827718",
                            "profilePicture": "https://attachments-public.clickup.com/profilePictures/183_abc.jpg"
                          },
                          "resolved": false,
                          "assignee": {
                            "id": 183,
                            "username": "John Doe",
                            "initials": "JD",
                            "email": "johndoe@gmail.com",
                            "color": "#827718",
                            "profilePicture": "https://attachments-public.clickup.com/profilePictures/183_abc.jpg"
                          },
                          "assigned_by": {
                            "id": 183,
                            "username": "John Doe",
                            "initials": "JD",
                            "email": "johndoe@gmail.com",
                            "color": "#827718",
                            "profilePicture": "https://attachments-public.clickup.com/profilePictures/183_abc.jpg"
                          },
                          "reactions": [],
                          "date": "1568036964079",
                          "reply_count": "1"
                        }
                      ]
                    }
                  ]
                },
                "example": {
                  "comments": [
                    {
                      "id": "462",
                      "comment": [
                        {
                          "text": "List comment content"
                        }
                      ],
                      "comment_text": "List comment content",
                      "user": {
                        "id": 183,
                        "username": "John Doe",
                        "initials": "JD",
                        "email": "johndoe@gmail.com",
                        "color": "#827718",
                        "profilePicture": "https://attachments-public.clickup.com/profilePictures/183_abc.jpg"
                      },
                      "resolved": false,
                      "assignee": {
                        "id": 183,
                        "username": "John Doe",
                        "initials": "JD",
                        "email": "johndoe@gmail.com",
                        "color": "#827718",
                        "profilePicture": "https://attachments-public.clickup.com/profilePictures/183_abc.jpg"
                      },
                      "assigned_by": {
                        "id": 183,
                        "username": "John Doe",
                        "initials": "JD",
                        "email": "johndoe@gmail.com",
                        "color": "#827718",
                        "profilePicture": "https://attachments-public.clickup.com/profilePictures/183_abc.jpg"
                      },
                      "reactions": [],
                      "date": "1568036964079",
                      "reply_count": "1"
                    }
                  ]
                }
              }
            }
          }
        },
        "deprecated": false
      },
      "parameters": []
    }
  },
  "components": {
    "securitySchemes": {
      "Authorization_Token": {
        "name": "Authorization",
        "type": "apiKey",
        "in": "header",
        "description": "API token required for authentication. Two types of tokens are supported:\n**Personal API Key** Obtain from ClickUp's settings page under 'Apps' and add it to the header as `Authorization: pk_...`\n**OAuth2 Access Token** Generated through the OAuth2 flow and add it to the header as `Authorization: Bearer {access_token}`"
      }
    }
  },
  "security": [
    {
      "Authorization_Token": []
    }
  ],
  "tags": [
    {
      "name": "Comments"
    }
  ]
}
```