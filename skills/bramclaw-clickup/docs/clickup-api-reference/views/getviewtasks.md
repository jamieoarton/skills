# Get View Tasks

See all visible tasks in a view in ClickUp.

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
    "/v2/view/{view_id}/task": {
      "get": {
        "summary": "Get View Tasks",
        "tags": [
          "Views"
        ],
        "description": "See all visible tasks in a view in ClickUp.",
        "operationId": "GetViewTasks",
        "parameters": [
          {
            "name": "view_id",
            "in": "path",
            "description": "105 (string)",
            "required": true,
            "style": "simple",
            "schema": {
              "type": "string",
              "examples": [
                "3c"
              ]
            }
          },
          {
            "name": "page",
            "in": "query",
            "description": "",
            "required": true,
            "style": "form",
            "explode": true,
            "schema": {
              "type": "integer",
              "contentEncoding": "int32",
              "examples": [
                0
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
                  "title": "GetViewTasksresponse",
                  "required": [
                    "tasks",
                    "last_page"
                  ],
                  "type": "object",
                  "properties": {
                    "tasks": {
                      "type": "array",
                      "items": {
                        "title": "Task9",
                        "type": "object",
                        "properties": {
                          "id": {
                            "type": "string"
                          },
                          "custom_item_id": {
                            "type": [
                              "number",
                              "null"
                            ]
                          },
                          "name": {
                            "type": "string"
                          },
                          "status": {
                            "$ref": "#/paths/~1v2~1task~1%7Btask_id%7D/get/responses/200/content/application~1json/schema/properties/status"
                          },
                          "markdown_description": {
                            "type": "string"
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
                          "date_done": {
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
                          "watchers": {
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
                            "$ref": "#/paths/~1v2~1task~1%7Btask_id%7D/get/responses/200/content/application~1json/schema/properties/priority"
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
                          "points": {
                            "type": [
                              "number"
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
                              "string"
                            ]
                          },
                          "custom_fields": {
                            "$ref": "#/paths/~1v2~1task~1%7Btask_id%7D/get/responses/200/content/application~1json/schema/properties/custom_fields/items"
                          },
                          "locations": {
                            "type": "array",
                            "items": {
                              "$ref": "#/paths/~1v2~1task~1%7Btask_id%7D/get/responses/200/content/application~1json/schema/properties/locations/items"
                            },
                            "description": "Array of Lists where the task has been added."
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
                          "url": {
                            "type": "string"
                          }
                        },
                        "examples": [
                          {
                            "id": "9hx",
                            "name": "New Task Name",
                            "custom_item_id": null,
                            "status": {
                              "status": "Open",
                              "color": "#d3d3d3",
                              "orderindex": 0,
                              "type": "open"
                            },
                            "markdown_description": "Task description",
                            "orderindex": "1.00000000000000000000000000000000",
                            "date_created": "1567780450202",
                            "date_updated": "1567780450202",
                            "date_closed": null,
                            "date_done": null,
                            "creator": {
                              "id": 183,
                              "username": "John Doe",
                              "color": "#827718",
                              "profilePicture": "https://attachments-public.clickup.com/profilePictures/183_abc.jpg"
                            },
                            "assignees": [],
                            "watchers": [],
                            "checklists": [],
                            "tags": [],
                            "parent": null,
                            "priority": {
                              "color": "#f8ae00",
                              "id": "3",
                              "orderindex": "3",
                              "priority": "normal"
                            },
                            "due_date": null,
                            "start_date": null,
                            "time_estimate": null,
                            "time_spent": 7200000,
                            "locations": [
                              {
                                "id": "123456",
                                "name": "Secondary List"
                              }
                            ],
                            "list": {
                              "id": "123"
                            },
                            "folder": {
                              "id": "456"
                            },
                            "space": {
                              "id": "789"
                            },
                            "url": "https://app.clickup.com/t/9hx"
                          }
                        ]
                      },
                      "description": ""
                    },
                    "last_page": {
                      "type": "boolean"
                    }
                  },
                  "examples": [
                    {
                      "tasks": [
                        {
                          "id": "9hx",
                          "name": "New Task Name",
                          "status": {
                            "status": "Open",
                            "color": "#d3d3d3",
                            "orderindex": 0,
                            "type": "open"
                          },
                          "orderindex": "1.00000000000000000000000000000000",
                          "date_created": "1567780450202",
                          "date_updated": "1567780450202",
                          "date_closed": null,
                          "date_done": null,
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
                          "priority": {
                            "color": "#f8ae00",
                            "id": "3",
                            "orderindex": "3",
                            "priority": "normal"
                          },
                          "due_date": null,
                          "start_date": null,
                          "points": 3,
                          "time_estimate": null,
                          "time_spent": null,
                          "custom_fields": {
                            "id": "0a52c486-5f05-403b-b4fd-c512ff05131c",
                            "name": "My Text Custom field",
                            "type": "text",
                            "type_config": {},
                            "date_created": "1622176979540",
                            "hide_from_guests": false,
                            "value": {
                              "value": "This is a string of text added to a Custom Field."
                            },
                            "required": true
                          },
                          "locations": [
                            {
                              "id": "123456",
                              "name": "Secondary List"
                            }
                          ],
                          "list": {
                            "id": "123"
                          },
                          "folder": {
                            "id": "456"
                          },
                          "space": {
                            "id": "789"
                          },
                          "url": "https://app.clickup.com/t/9hx"
                        },
                        {
                          "id": "9hz",
                          "name": "Second task",
                          "status": {
                            "status": "Open",
                            "color": "#d3d3d3",
                            "orderindex": 0,
                            "type": "open"
                          },
                          "orderindex": "2.00000000000000000000000000000000",
                          "date_created": "1567780450202",
                          "date_updated": "1567780450202",
                          "date_closed": null,
                          "date_done": null,
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
                          "points": 3,
                          "time_estimate": null,
                          "time_spent": null,
                          "custom_fields": {
                            "id": "0a52c486-5f05-403b-b4fd-c512ff05131c",
                            "name": "My Text Custom field",
                            "type": "text",
                            "type_config": {},
                            "date_created": "1622176979540",
                            "hide_from_guests": false,
                            "value": {
                              "value": "This is a string of text added to a Custom Field."
                            },
                            "required": true
                          },
                          "locations": [],
                          "list": {
                            "id": "123"
                          },
                          "folder": {
                            "id": "456"
                          },
                          "space": {
                            "id": "789"
                          },
                          "url": "https://app.clickup.com/t/9hz"
                        }
                      ],
                      "last_page": true
                    }
                  ]
                },
                "example": {
                  "tasks": [
                    {
                      "id": "9hx",
                      "name": "New Task Name",
                      "status": {
                        "status": "Open",
                        "color": "#d3d3d3",
                        "orderindex": 0,
                        "type": "open"
                      },
                      "orderindex": "1.00000000000000000000000000000000",
                      "date_created": "1567780450202",
                      "date_updated": "1567780450202",
                      "date_closed": null,
                      "date_done": null,
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
                      "priority": {
                        "color": "#f8ae00",
                        "id": "3",
                        "orderindex": "3",
                        "priority": "normal"
                      },
                      "due_date": null,
                      "start_date": null,
                      "points": 3,
                      "time_estimate": null,
                      "time_spent": null,
                      "custom_fields": {
                        "id": "0a52c486-5f05-403b-b4fd-c512ff05131c",
                        "name": "My Text Custom field",
                        "type": "text",
                        "type_config": {},
                        "date_created": "1622176979540",
                        "hide_from_guests": false,
                        "value": {
                          "value": "This is a string of text added to a Custom Field."
                        },
                        "required": true
                      },
                      "locations": [
                        {
                          "id": "123456",
                          "name": "Secondary List"
                        }
                      ],
                      "list": {
                        "id": "123"
                      },
                      "folder": {
                        "id": "456"
                      },
                      "space": {
                        "id": "789"
                      },
                      "url": "https://app.clickup.com/t/9hx"
                    },
                    {
                      "id": "9hz",
                      "name": "Second task",
                      "status": {
                        "status": "Open",
                        "color": "#d3d3d3",
                        "orderindex": 0,
                        "type": "open"
                      },
                      "orderindex": "2.00000000000000000000000000000000",
                      "date_created": "1567780450202",
                      "date_updated": "1567780450202",
                      "date_closed": null,
                      "date_done": null,
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
                      "points": 3,
                      "time_estimate": null,
                      "time_spent": null,
                      "custom_fields": {
                        "id": "0a52c486-5f05-403b-b4fd-c512ff05131c",
                        "name": "My Text Custom field",
                        "type": "text",
                        "type_config": {},
                        "date_created": "1622176979540",
                        "hide_from_guests": false,
                        "value": {
                          "value": "This is a string of text added to a Custom Field."
                        },
                        "required": true
                      },
                      "locations": [],
                      "list": {
                        "id": "123"
                      },
                      "folder": {
                        "id": "456"
                      },
                      "space": {
                        "id": "789"
                      },
                      "url": "https://app.clickup.com/t/9hz"
                    }
                  ],
                  "last_page": true
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
      "name": "Views"
    }
  ]
}
```