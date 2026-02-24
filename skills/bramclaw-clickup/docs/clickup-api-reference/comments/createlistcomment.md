# Create List Comment

Add a comment to a List.

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
      "post": {
        "summary": "Create List Comment",
        "tags": [
          "Comments"
        ],
        "description": "Add a comment to a List.",
        "operationId": "CreateListComment",
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
          }
        ],
        "requestBody": {
          "description": "",
          "content": {
            "application/json": {
              "schema": {
                "title": "CreateListCommentrequest",
                "required": [
                  "comment_text",
                  "assignee",
                  "notify_all"
                ],
                "type": "object",
                "properties": {
                  "comment_text": {
                    "type": "string"
                  },
                  "assignee": {
                    "type": "integer",
                    "contentEncoding": "int32"
                  },
                  "notify_all": {
                    "description": "If `notify_all` is true, notifications will be sent to everyone including the creator of the comment.",
                    "type": "boolean"
                  }
                },
                "examples": [
                  {
                    "comment_text": "List comment content",
                    "assignee": 183,
                    "notify_all": true
                  }
                ]
              },
              "example": {
                "comment_text": "List comment content",
                "assignee": 183,
                "notify_all": true
              }
            }
          },
          "required": true
        },
        "responses": {
          "200": {
            "description": "",
            "headers": {},
            "content": {
              "application/json": {
                "schema": {
                  "title": "CreateListCommentresponse",
                  "required": [
                    "id",
                    "hist_id",
                    "date"
                  ],
                  "type": "object",
                  "properties": {
                    "id": {
                      "type": "string"
                    },
                    "hist_id": {
                      "type": "string"
                    },
                    "date": {
                      "type": "integer",
                      "contentEncoding": "int64"
                    }
                  },
                  "examples": [
                    {
                      "id": "462",
                      "hist_id": "5bbea9ad-7cc3-4038-a8bb-a89ac1337c08",
                      "date": 1568037341249
                    }
                  ]
                },
                "example": {
                  "id": "462",
                  "hist_id": "5bbea9ad-7cc3-4038-a8bb-a89ac1337c08",
                  "date": 1568037341249
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