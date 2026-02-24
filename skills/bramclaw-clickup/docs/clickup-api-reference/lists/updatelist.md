# Update List

Rename a List, update the List Info description, set a due date/time, set the List's priority, set an assignee, set or remove the List color.

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
    "/v2/list/{list_id}": {
      "put": {
        "summary": "Update List",
        "tags": [
          "Lists"
        ],
        "description": "Rename a List, update the List Info description, set a due date/time, set the List's priority, set an assignee, set or remove the List color.",
        "operationId": "UpdateList",
        "parameters": [
          {
            "name": "list_id",
            "in": "path",
            "description": "",
            "required": true,
            "style": "simple",
            "schema": {
              "type": "string",
              "examples": [
                "124"
              ]
            }
          }
        ],
        "requestBody": {
          "description": "",
          "content": {
            "application/json": {
              "schema": {
                "title": "UpdateListrequest",
                "required": [
                  "name"
                ],
                "type": "object",
                "properties": {
                  "name": {
                    "type": "string"
                  },
                  "content": {
                    "type": "string"
                  },
                  "markdown_content": {
                    "type": "string",
                    "description": "Use `markdown_content` instead of `content` to format your List description."
                  },
                  "due_date": {
                    "type": "integer",
                    "contentEncoding": "int64"
                  },
                  "due_date_time": {
                    "type": "boolean"
                  },
                  "priority": {
                    "type": "integer",
                    "contentEncoding": "int32"
                  },
                  "assignee": {
                    "type": "string"
                  },
                  "status": {
                    "description": "**Status** refers to the List color rather than the task Statuses available in the List.",
                    "type": "string"
                  },
                  "unset_status": {
                    "description": "By default, this is `false.` To remove the List color use `unset_status: true`.",
                    "type": "boolean"
                  }
                },
                "examples": [
                  {
                    "name": "Updated List Name",
                    "content": "Updated List Content",
                    "markdown_content": "# This is markdown\n ***bold and italicized text***",
                    "due_date": 1567780450202,
                    "due_date_time": true,
                    "priority": 2,
                    "assignee": "none",
                    "status": "red",
                    "unset_status": true
                  }
                ]
              },
              "example": {
                "name": "Updated List Name",
                "content": "Updated List Content",
                "markdown_content": "# This is markdown\n ***bold and italicized text***",
                "due_date": 1567780450202,
                "due_date_time": true,
                "priority": 2,
                "assignee": "none",
                "status": "red",
                "unset_status": true
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
                  "title": "UpdateListresponse",
                  "type": "object",
                  "properties": {
                    "id": {
                      "type": "string"
                    },
                    "name": {
                      "type": "string"
                    },
                    "orderindex": {
                      "type": "integer",
                      "contentEncoding": "int32"
                    },
                    "content": {
                      "type": "string"
                    },
                    "status": {
                      "$ref": "#/paths/~1v2~1list~1%7Blist_id%7D/get/responses/200/content/application~1json/schema/properties/status"
                    },
                    "priority": {
                      "$ref": "#/paths/~1v2~1list~1%7Blist_id%7D/get/responses/200/content/application~1json/schema/properties/priority"
                    },
                    "assignee": {
                      "type": [
                        "string",
                        "null"
                      ]
                    },
                    "task_count": {
                      "type": [
                        "string",
                        "null"
                      ]
                    },
                    "due_date": {
                      "type": "string"
                    },
                    "due_date_time": {
                      "type": "boolean"
                    },
                    "start_date": {
                      "type": [
                        "string",
                        "null"
                      ]
                    },
                    "start_date_time": {
                      "type": [
                        "string",
                        "null"
                      ]
                    },
                    "folder": {
                      "$ref": "#/paths/~1v2~1list~1%7Blist_id%7D/get/responses/200/content/application~1json/schema/properties/folder"
                    },
                    "space": {
                      "$ref": "#/paths/~1v2~1list~1%7Blist_id%7D/get/responses/200/content/application~1json/schema/properties/space"
                    },
                    "statuses": {
                      "type": "array",
                      "items": {
                        "$ref": "#/paths/~1v2~1task~1%7Btask_id%7D/get/responses/200/content/application~1json/schema/properties/status"
                      },
                      "description": ""
                    },
                    "inbound_address": {
                      "type": "string"
                    }
                  },
                  "examples": [
                    {
                      "id": "124",
                      "name": "Updated List Name",
                      "orderindex": 1,
                      "content": "Updated List Content",
                      "status": {
                        "status": "red",
                        "color": "#e50000",
                        "hide_label": true
                      },
                      "priority": {
                        "priority": "high",
                        "color": "#f50000"
                      },
                      "assignee": null,
                      "task_count": null,
                      "due_date": "1567780450202",
                      "due_date_time": true,
                      "start_date": null,
                      "start_date_time": null,
                      "folder": {
                        "id": "456",
                        "name": "Folder Name",
                        "hidden": false,
                        "access": true
                      },
                      "space": {
                        "id": "789",
                        "name": "Space Name",
                        "access": true
                      },
                      "statuses": [
                        {
                          "status": "to do",
                          "orderindex": 0,
                          "color": "#d3d3d3",
                          "type": "open"
                        },
                        {
                          "status": "complete",
                          "orderindex": 1,
                          "color": "#6bc950",
                          "type": "closed"
                        }
                      ],
                      "inbound_address": "add.task.1389.ac725f.31518a6a-05bb-4997-92a6-1dcfe2f527ca@tasks.clickup.com"
                    }
                  ]
                },
                "example": {
                  "id": "124",
                  "name": "Updated List Name",
                  "orderindex": 1,
                  "content": "Updated List Content",
                  "status": {
                    "status": "red",
                    "color": "#e50000",
                    "hide_label": true
                  },
                  "priority": {
                    "priority": "high",
                    "color": "#f50000"
                  },
                  "assignee": null,
                  "task_count": null,
                  "due_date": "1567780450202",
                  "due_date_time": true,
                  "start_date": null,
                  "start_date_time": null,
                  "folder": {
                    "id": "456",
                    "name": "Folder Name",
                    "hidden": false,
                    "access": true
                  },
                  "space": {
                    "id": "789",
                    "name": "Space Name",
                    "access": true
                  },
                  "statuses": [
                    {
                      "status": "to do",
                      "orderindex": 0,
                      "color": "#d3d3d3",
                      "type": "open"
                    },
                    {
                      "status": "complete",
                      "orderindex": 1,
                      "color": "#6bc950",
                      "type": "closed"
                    }
                  ],
                  "inbound_address": "add.task.1389.ac725f.31518a6a-05bb-4997-92a6-1dcfe2f527ca@tasks.clickup.com"
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
      "name": "Lists"
    }
  ]
}
```