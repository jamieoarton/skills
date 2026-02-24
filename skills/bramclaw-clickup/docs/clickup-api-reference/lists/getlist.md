# Get List

View information about a List.

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
      "get": {
        "summary": "Get List",
        "tags": [
          "Lists"
        ],
        "description": "View information about a List.",
        "operationId": "GetList",
        "parameters": [
          {
            "name": "list_id",
            "in": "path",
            "description": "The List ID. To find the List ID, right-click the List in your Sidebar, select Copy link, and paste the link in your URL. The last string in the URL is your List ID.",
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
        "responses": {
          "200": {
            "description": "",
            "headers": {},
            "content": {
              "application/json": {
                "schema": {
                  "title": "GetListresponse",
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
                      "title": "Status5",
                      "required": [
                        "status",
                        "color",
                        "hide_label"
                      ],
                      "type": "object",
                      "properties": {
                        "status": {
                          "type": "string"
                        },
                        "color": {
                          "type": "string"
                        },
                        "hide_label": {
                          "type": "boolean"
                        }
                      },
                      "examples": [
                        {
                          "status": "red",
                          "color": "#e50000",
                          "hide_label": true
                        }
                      ]
                    },
                    "priority": {
                      "title": "Priority1",
                      "required": [
                        "priority",
                        "color"
                      ],
                      "type": "object",
                      "properties": {
                        "priority": {
                          "type": "string"
                        },
                        "color": {
                          "type": "string"
                        }
                      },
                      "examples": [
                        {
                          "priority": "urgent",
                          "color": "#f50000"
                        }
                      ]
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
                      "title": "Folder3",
                      "required": [
                        "id",
                        "name",
                        "hidden",
                        "access"
                      ],
                      "type": "object",
                      "properties": {
                        "id": {
                          "type": "string"
                        },
                        "name": {
                          "type": "string"
                        },
                        "hidden": {
                          "type": "boolean"
                        },
                        "access": {
                          "type": "boolean"
                        }
                      },
                      "examples": [
                        {
                          "id": "1217",
                          "name": "Shared with me",
                          "hidden": false,
                          "access": false
                        }
                      ]
                    },
                    "space": {
                      "title": "Space2",
                      "required": [
                        "id",
                        "name",
                        "access"
                      ],
                      "type": "object",
                      "properties": {
                        "id": {
                          "type": "string"
                        },
                        "name": {
                          "type": "string"
                        },
                        "access": {
                          "type": "boolean"
                        }
                      },
                      "examples": [
                        {
                          "id": "789",
                          "name": "Space Name",
                          "access": true
                        }
                      ]
                    },
                    "inbound_address": {
                      "type": "string"
                    },
                    "archived": {
                      "type": "boolean"
                    },
                    "override_statuses": {
                      "type": "boolean"
                    },
                    "statuses": {
                      "type": "array",
                      "items": {
                        "$ref": "#/paths/~1v2~1task~1%7Btask_id%7D/get/responses/200/content/application~1json/schema/properties/status"
                      },
                      "description": ""
                    },
                    "permission_level": {
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
                      "inbound_address": "add.task.124.ac725f.31518a6a-05bb-4997-92a6-1dcfe2f527ca@tasks.clickup.com",
                      "archived": false,
                      "override_statuses": false,
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
                      "permission_level": "create"
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
                  "task_count": 10,
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
                  "inbound_address": "add.task.124.ac725f.31518a6a-05bb-4997-92a6-1dcfe2f527ca@tasks.clickup.com",
                  "archived": false,
                  "override_statuses": false,
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
                  "permission_level": "create"
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