# Create Task Comment

Add a new comment to a task.

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
    "/v2/task/{task_id}/comment": {
      "post": {
        "summary": "Create Task Comment",
        "tags": [
          "Comments"
        ],
        "description": "Add a new comment to a task.",
        "operationId": "CreateTaskComment",
        "parameters": [
          {
            "name": "task_id",
            "in": "path",
            "description": "",
            "required": true,
            "style": "simple",
            "schema": {
              "type": "string",
              "examples": [
                "9hz"
              ]
            }
          },
          {
            "name": "custom_task_ids",
            "in": "query",
            "description": "If you want to reference a task by it's custom task id, this value must be `true`.",
            "style": "form",
            "explode": true,
            "schema": {
              "type": "boolean",
              "examples": [
                true
              ]
            }
          },
          {
            "name": "team_id",
            "in": "query",
            "description": "When the `custom_task_ids` parameter is set to `true`, the Workspace ID must be provided using the `team_id` parameter.\n \\\nFor example: `custom_task_ids=true&team_id=123`.",
            "style": "form",
            "explode": true,
            "schema": {
              "type": "number",
              "contentEncoding": "double",
              "examples": [
                123
              ]
            }
          }
        ],
        "requestBody": {
          "description": "",
          "content": {
            "application/json": {
              "schema": {
                "title": "CreateTaskCommentrequest",
                "required": [
                  "comment_text",
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
                  "group_assignee": {
                    "type": "string",
                    "contentEncoding": "int32",
                    "description": ""
                  },
                  "notify_all": {
                    "description": "If `notify_all` is true, notifications will be sent to everyone including the creator of the comment.",
                    "type": "boolean"
                  }
                },
                "examples": [
                  {
                    "comment_text": "Task comment content",
                    "assignee": 183,
                    "group_assignee": "d01f92f-48ca-446d-88a1-0beb0e8f5f14",
                    "notify_all": true
                  }
                ]
              },
              "example": {
                "comment_text": "Task comment content",
                "assignee": 183,
                "group_assignee": "dd01f92f-48ca-446d-88a1-0beb0e8f5f14",
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
                  "title": "CreateTaskCommentresponse",
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
                      "id": "458",
                      "hist_id": "26508",
                      "date": 1568036964079
                    }
                  ]
                },
                "example": {
                  "id": "458",
                  "hist_id": "26508",
                  "date": 1568036964079
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