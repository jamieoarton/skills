# Add Task Link

This is the equivalent of the feature _Task Links_ in the right-hand sidebar of a Task.  It allows you to link two tasks together. General links or links to other objects than tasks are not supported.

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
    "/v2/task/{task_id}/link/{links_to}": {
      "post": {
        "summary": "Add Task Link",
        "tags": [
          "Task Relationships"
        ],
        "description": "This is the equivalent of the feature _Task Links_ in the right-hand sidebar of a Task.  It allows you to link two tasks together. General links or links to other objects than tasks are not supported.",
        "operationId": "AddTaskLink",
        "parameters": [
          {
            "name": "task_id",
            "in": "path",
            "description": "The task to initiate the link from.",
            "required": true,
            "style": "simple",
            "schema": {
              "type": "string",
              "examples": [
                "9hv"
              ]
            }
          },
          {
            "name": "links_to",
            "in": "path",
            "description": "The task to link to.",
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
        "responses": {
          "200": {
            "description": "",
            "headers": {},
            "content": {
              "application/json": {
                "schema": {
                  "title": "AddTaskLinkresponse",
                  "required": [
                    "task"
                  ],
                  "type": "object",
                  "properties": {
                    "task": {
                      "title": "Task",
                      "required": [
                        "id",
                        "name",
                        "status",
                        "orderindex",
                        "date_created",
                        "date_updated",
                        "date_closed",
                        "creator",
                        "assignees",
                        "checklists",
                        "tags",
                        "parent",
                        "priority",
                        "due_date",
                        "start_date",
                        "time_estimate",
                        "time_spent",
                        "list",
                        "folder",
                        "space",
                        "linked_tasks",
                        "url"
                      ],
                      "type": "object",
                      "properties": {
                        "id": {
                          "type": "string"
                        },
                        "name": {
                          "type": "string"
                        },
                        "status": {
                          "$ref": "#/paths/~1v2~1task~1%7Btask_id%7D/get/responses/200/content/application~1json/schema/properties/status"
                        },
                        "orderindex": {
                          "type": "string"
                        },
                        "date_created": {
                          "type": "string"
                        },
                        "date_updated": {
                          "type": "string"
                        },
                        "date_closed": {
                          "type": [
                            "string",
                            "null"
                          ]
                        },
                        "creator": {
                          "$ref": "#/paths/~1v2~1task~1%7Btask_id%7D/get/responses/200/content/application~1json/schema/properties/creator"
                        },
                        "assignees": {
                          "type": "array",
                          "items": {
                            "type": "string"
                          },
                          "description": ""
                        },
                        "checklists": {
                          "type": "array",
                          "items": {
                            "type": "string"
                          },
                          "description": ""
                        },
                        "tags": {
                          "type": "array",
                          "items": {
                            "type": "string"
                          },
                          "description": ""
                        },
                        "parent": {
                          "type": [
                            "string",
                            "null"
                          ]
                        },
                        "priority": {
                          "type": [
                            "string",
                            "null"
                          ]
                        },
                        "due_date": {
                          "type": [
                            "string",
                            "null"
                          ]
                        },
                        "start_date": {
                          "type": [
                            "string",
                            "null"
                          ]
                        },
                        "time_estimate": {
                          "type": [
                            "string",
                            "null"
                          ]
                        },
                        "time_spent": {
                          "type": [
                            "string",
                            "null"
                          ]
                        },
                        "list": {
                          "$ref": "#/paths/~1v2~1task~1%7Btask_id%7D/get/responses/200/content/application~1json/schema/properties/list"
                        },
                        "folder": {
                          "$ref": "#/paths/~1v2~1task~1%7Btask_id%7D/get/responses/200/content/application~1json/schema/properties/folder"
                        },
                        "space": {
                          "$ref": "#/paths/~1v2~1task~1%7Btask_id%7D/get/responses/200/content/application~1json/schema/properties/space"
                        },
                        "linked_tasks": {
                          "type": "array",
                          "items": {
                            "title": "LinkedTask",
                            "required": [
                              "task_id",
                              "link_id",
                              "date_created",
                              "userid"
                            ],
                            "type": "object",
                            "properties": {
                              "task_id": {
                                "type": "string"
                              },
                              "link_id": {
                                "type": "string"
                              },
                              "date_created": {
                                "type": "string"
                              },
                              "userid": {
                                "type": "string"
                              }
                            },
                            "examples": [
                              {
                                "task_id": "9hv",
                                "link_id": "9hz",
                                "date_created": "1587571108988",
                                "userid": "183"
                              }
                            ]
                          },
                          "description": ""
                        },
                        "url": {
                          "type": "string"
                        }
                      },
                      "examples": [
                        {
                          "id": "9hv",
                          "name": "Task Name",
                          "status": {
                            "status": "in progress",
                            "color": "#d3d3d3",
                            "orderindex": 1,
                            "type": "custom"
                          },
                          "orderindex": "1.00000000000000000000000000000000",
                          "date_created": "1567780450202",
                          "date_updated": "1567780450202",
                          "date_closed": null,
                          "creator": {
                            "id": 183,
                            "username": "John Doe",
                            "color": "#827718",
                            "profilePicture": "https://attachments-public.clickup.com/profilePictures/183_abc.jpg"
                          },
                          "assignees": [],
                          "checklists": [],
                          "tags": [],
                          "parent": null,
                          "priority": null,
                          "due_date": null,
                          "start_date": null,
                          "time_estimate": null,
                          "time_spent": null,
                          "list": {
                            "id": "123"
                          },
                          "folder": {
                            "id": "456"
                          },
                          "space": {
                            "id": "789"
                          },
                          "linked_tasks": [
                            {
                              "task_id": "9hv",
                              "link_id": "9hz",
                              "date_created": "1587571108988",
                              "userid": "183"
                            }
                          ],
                          "url": "https://app.clickup.com/t/9hx"
                        }
                      ]
                    }
                  },
                  "examples": [
                    {
                      "task": {
                        "id": "9hv",
                        "name": "Task Name",
                        "status": {
                          "status": "in progress",
                          "color": "#d3d3d3",
                          "orderindex": 1,
                          "type": "custom"
                        },
                        "orderindex": "1.00000000000000000000000000000000",
                        "date_created": "1567780450202",
                        "date_updated": "1567780450202",
                        "date_closed": null,
                        "creator": {
                          "id": 183,
                          "username": "John Doe",
                          "color": "#827718",
                          "profilePicture": "https://attachments-public.clickup.com/profilePictures/183_abc.jpg"
                        },
                        "assignees": [],
                        "checklists": [],
                        "tags": [],
                        "parent": null,
                        "priority": null,
                        "due_date": null,
                        "start_date": null,
                        "time_estimate": null,
                        "time_spent": null,
                        "list": {
                          "id": "123"
                        },
                        "folder": {
                          "id": "456"
                        },
                        "space": {
                          "id": "789"
                        },
                        "linked_tasks": [
                          {
                            "task_id": "9hv",
                            "link_id": "9hz",
                            "date_created": "1587571108988",
                            "userid": "183"
                          }
                        ],
                        "url": "https://app.clickup.com/t/9hx"
                      }
                    }
                  ]
                },
                "example": {
                  "task": {
                    "id": "9hv",
                    "name": "Task Name",
                    "status": {
                      "status": "in progress",
                      "color": "#d3d3d3",
                      "orderindex": 1,
                      "type": "custom"
                    },
                    "orderindex": "1.00000000000000000000000000000000",
                    "date_created": "1567780450202",
                    "date_updated": "1567780450202",
                    "date_closed": null,
                    "creator": {
                      "id": 183,
                      "username": "John Doe",
                      "color": "#827718",
                      "profilePicture": "https://attachments-public.clickup.com/profilePictures/183_abc.jpg"
                    },
                    "assignees": [],
                    "checklists": [],
                    "tags": [],
                    "parent": null,
                    "priority": null,
                    "due_date": null,
                    "start_date": null,
                    "time_estimate": null,
                    "time_spent": null,
                    "list": {
                      "id": "123"
                    },
                    "folder": {
                      "id": "456"
                    },
                    "space": {
                      "id": "789"
                    },
                    "linked_tasks": [
                      {
                        "task_id": "9hv",
                        "link_id": "9hz",
                        "date_created": "1587571108988",
                        "userid": "183"
                      }
                    ],
                    "url": "https://app.clickup.com/t/9hx"
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
      "name": "Task Relationships"
    }
  ]
}
```