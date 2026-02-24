# Update Webhook

Update a webhook to change the events to be monitored.

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
    "/v2/webhook/{webhook_id}": {
      "put": {
        "summary": "Update Webhook",
        "tags": [
          "Webhooks"
        ],
        "description": "Update a webhook to change the events to be monitored.",
        "operationId": "UpdateWebhook",
        "parameters": [
          {
            "name": "webhook_id",
            "in": "path",
            "description": "e506-4a29-9d42-26e504e3435e (uuid)",
            "required": true,
            "style": "simple",
            "schema": {
              "type": "string",
              "examples": [
                "4b67ac88"
              ]
            }
          }
        ],
        "requestBody": {
          "description": "To subscribe to specific events, pass an array of `events` that you want to subscribe to, or use the wildcard character `\"*\"` to subscribe to everything.\\\n \\\nIf you don't specify any events, all events will be sent to the webhook.",
          "content": {
            "application/json": {
              "schema": {
                "title": "UpdateWebhookrequest",
                "required": [
                  "endpoint",
                  "events",
                  "status"
                ],
                "type": "object",
                "properties": {
                  "endpoint": {
                    "type": "string"
                  },
                  "events": {
                    "type": "string"
                  },
                  "status": {
                    "type": "string"
                  }
                },
                "examples": [
                  {
                    "endpoint": "https://yourdomain.com/webhook",
                    "events": "*",
                    "status": "active"
                  }
                ]
              },
              "example": {
                "endpoint": "https://yourdomain.com/webhook",
                "events": "*",
                "status": "active"
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
                  "title": "UpdateWebhookresponse",
                  "required": [
                    "id",
                    "webhook"
                  ],
                  "type": "object",
                  "properties": {
                    "id": {
                      "type": "string"
                    },
                    "webhook": {
                      "title": "Webhook",
                      "required": [
                        "id",
                        "userid",
                        "team_id",
                        "endpoint",
                        "client_id",
                        "events",
                        "task_id",
                        "list_id",
                        "folder_id",
                        "space_id",
                        "health",
                        "secret"
                      ],
                      "type": "object",
                      "properties": {
                        "id": {
                          "type": "string"
                        },
                        "userid": {
                          "type": "integer",
                          "contentEncoding": "int32"
                        },
                        "team_id": {
                          "type": "integer",
                          "contentEncoding": "int32"
                        },
                        "endpoint": {
                          "type": "string"
                        },
                        "client_id": {
                          "type": "string"
                        },
                        "events": {
                          "type": "array",
                          "items": {
                            "type": "string"
                          },
                          "description": ""
                        },
                        "task_id": {
                          "type": [
                            "string",
                            "null"
                          ]
                        },
                        "list_id": {
                          "type": [
                            "string",
                            "null"
                          ]
                        },
                        "folder_id": {
                          "type": [
                            "string",
                            "null"
                          ]
                        },
                        "space_id": {
                          "type": [
                            "string",
                            "null"
                          ]
                        },
                        "health": {
                          "title": "Health",
                          "required": [
                            "status",
                            "fail_count"
                          ],
                          "type": "object",
                          "properties": {
                            "status": {
                              "type": "string"
                            },
                            "fail_count": {
                              "type": "integer",
                              "contentEncoding": "int32"
                            }
                          },
                          "examples": [
                            {
                              "status": "active",
                              "fail_count": 0
                            }
                          ]
                        },
                        "secret": {
                          "type": "string"
                        }
                      },
                      "examples": [
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
                            "status": "active",
                            "fail_count": 0
                          },
                          "secret": "O94IM25S7PXBPYTMNXLLET230SRP0S89COR7B1YOJ2ZIE8WQNK5UUKEF26W0Z5GA"
                        }
                      ]
                    }
                  },
                  "examples": [
                    {
                      "id": "4b67ac88-e506-4a29-9d42-26e504e3435e",
                      "webhook": {
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
                          "status": "active",
                          "fail_count": 0
                        },
                        "secret": "O94IM25S7PXBPYTMNXLLET230SRP0S89COR7B1YOJ2ZIE8WQNK5UUKEF26W0Z5GA"
                      }
                    }
                  ]
                },
                "example": {
                  "id": "4b67ac88-e506-4a29-9d42-26e504e3435e",
                  "webhook": {
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
                      "status": "active",
                      "fail_count": 0
                    },
                    "secret": "O94IM25S7PXBPYTMNXLLET230SRP0S89COR7B1YOJ2ZIE8WQNK5UUKEF26W0Z5GA"
                  }
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