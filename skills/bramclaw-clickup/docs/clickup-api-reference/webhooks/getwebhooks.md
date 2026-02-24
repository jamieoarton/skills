# Get Webhooks

View the webhooks created via the API for a Workspace. This endpoint returns webhooks created by the authenticated user.

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
    "/v2/team/{team_id}/webhook": {
      "get": {
        "summary": "Get Webhooks",
        "tags": [
          "Webhooks"
        ],
        "description": "View the webhooks created via the API for a Workspace. This endpoint returns webhooks created by the authenticated user.",
        "operationId": "GetWebhooks",
        "parameters": [
          {
            "name": "team_id",
            "in": "path",
            "description": "Workspace ID",
            "required": true,
            "style": "simple",
            "schema": {
              "type": "number",
              "contentEncoding": "double",
              "examples": [
                123
              ]
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
                  "title": "GetWebhooksresponse",
                  "required": [
                    "webhooks"
                  ],
                  "type": "object",
                  "properties": {
                    "webhooks": {
                      "type": "array",
                      "items": {
                        "$ref": "#/paths/~1v2~1webhook~1%7Bwebhook_id%7D/put/responses/200/content/application~1json/schema/properties/webhook"
                      },
                      "description": ""
                    }
                  },
                  "examples": [
                    {
                      "webhooks": [
                        {
                          "id": "4b67ac88-e506-4a29-9d42-26e504e3435e",
                          "userid": 183,
                          "team_id": 108,
                          "endpoint": "https://yourdomain.com/webhook",
                          "client_id": "QVOQP06ZXC6CMGVFKB0ZT7J9Y7APOYGO",
                          "events": [
                            "taskCreated",
                            "taskUpdated",
                            "taskDeleted",
                            "taskPriorityUpdated",
                            "taskStatusUpdated",
                            "taskAssigneeUpdated",
                            "taskDueDateUpdated",
                            "taskTagUpdated",
                            "taskMoved",
                            "taskCommentPosted",
                            "taskCommentUpdated",
                            "taskTimeEstimateUpdated",
                            "taskTimeTrackedUpdated",
                            "listCreated",
                            "listUpdated",
                            "listDeleted",
                            "folderCreated",
                            "folderUpdated",
                            "folderDeleted",
                            "spaceCreated",
                            "spaceUpdated",
                            "spaceDeleted",
                            "goalCreated",
                            "goalUpdated",
                            "goalDeleted",
                            "keyResultCreated",
                            "keyResultUpdated",
                            "keyResultDeleted"
                          ],
                          "task_id": null,
                          "list_id": null,
                          "folder_id": null,
                          "space_id": null,
                          "health": {
                            "status": "failing",
                            "fail_count": 5
                          },
                          "secret": "O94IM25S7PXBPYTMNXLLET230SRP0S89COR7B1YOJ2ZIE8WQNK5UUKEF26W0Z5GA"
                        }
                      ]
                    }
                  ]
                },
                "example": {
                  "webhooks": [
                    {
                      "id": "4b67ac88-e506-4a29-9d42-26e504e3435e",
                      "userid": 183,
                      "team_id": 108,
                      "endpoint": "https://yourdomain.com/webhook",
                      "client_id": "QVOQP06ZXC6CMGVFKB0ZT7J9Y7APOYGO",
                      "events": [
                        "taskCreated",
                        "taskUpdated",
                        "taskDeleted",
                        "taskPriorityUpdated",
                        "taskStatusUpdated",
                        "taskAssigneeUpdated",
                        "taskDueDateUpdated",
                        "taskTagUpdated",
                        "taskMoved",
                        "taskCommentPosted",
                        "taskCommentUpdated",
                        "taskTimeEstimateUpdated",
                        "taskTimeTrackedUpdated",
                        "listCreated",
                        "listUpdated",
                        "listDeleted",
                        "folderCreated",
                        "folderUpdated",
                        "folderDeleted",
                        "spaceCreated",
                        "spaceUpdated",
                        "spaceDeleted",
                        "goalCreated",
                        "goalUpdated",
                        "goalDeleted",
                        "keyResultCreated",
                        "keyResultUpdated",
                        "keyResultDeleted"
                      ],
                      "task_id": null,
                      "list_id": null,
                      "folder_id": null,
                      "space_id": null,
                      "health": {
                        "status": "failing",
                        "fail_count": 5
                      },
                      "secret": "O94IM25S7PXBPYTMNXLLET230SRP0S89COR7B1YOJ2ZIE8WQNK5UUKEF26W0Z5GA"
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
      "name": "Webhooks"
    }
  ]
}
```