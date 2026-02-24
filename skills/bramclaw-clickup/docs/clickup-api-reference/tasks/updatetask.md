# Update Task

Update a task by including one or more fields in the request body.

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
    "/v2/task/{task_id}": {
      "put": {
        "summary": "Update Task",
        "tags": [
          "Tasks"
        ],
        "description": "Update a task by including one or more fields in the request body.",
        "operationId": "UpdateTask",
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
                "9hx"
              ]
            }
          },
          {
            "name": "custom_task_ids",
            "in": "query",
            "description": "If you want to reference a task by its custom task id, this value must be `true`.",
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
          "description": "***Note:** To update Custom Fields on a task, you must use the Set Custom Field endpoint.*",
          "content": {
            "application/json": {
              "schema": {
                "title": "UpdateTaskrequest",
                "type": "object",
                "properties": {
                  "custom_item_id": {
                    "type": [
                      "number",
                      "null"
                    ],
                    "description": "The custom task type ID for this task. A value of `null` (default) sets the task type to type \"Task\".\\\n \\\nTo get a list of available custom task type IDs for your Workspace, use the [Get Custom Task Types endpoint](https://developer.clickup.com/reference/getcustomitems)."
                  },
                  "name": {
                    "type": "string"
                  },
                  "description": {
                    "description": "To clear the task description, include `Description` with `\" \"`.",
                    "type": "string"
                  },
                  "markdown_content": {
                    "type": "string",
                    "description": "Markdown formatted description for the task. If both `markdown_content` and `description` are provided, `markdown_content` will be used instead of `description`."
                  },
                  "status": {
                    "type": "string"
                  },
                  "priority": {
                    "type": "integer",
                    "contentEncoding": "int32"
                  },
                  "due_date": {
                    "type": "integer",
                    "contentEncoding": "int64"
                  },
                  "due_date_time": {
                    "type": "boolean"
                  },
                  "parent": {
                    "description": "You can move a subtask to another parent task by including `\"parent\"` with a valid `task id`.\\\n \\\nYou cannot convert a subtask to a task by setting `\"parent\"` to `null`.",
                    "type": "string"
                  },
                  "time_estimate": {
                    "type": "integer",
                    "contentEncoding": "int32"
                  },
                  "start_date": {
                    "type": "integer",
                    "contentEncoding": "int64"
                  },
                  "start_date_time": {
                    "type": "boolean"
                  },
                  "points": {
                    "type": "number",
                    "description": "Update the task's Sprint Points."
                  },
                  "assignees": {
                    "title": "Assignees",
                    "required": [
                      "add",
                      "rem"
                    ],
                    "type": "object",
                    "properties": {
                      "add": {
                        "type": "array",
                        "items": {
                          "type": "integer",
                          "contentEncoding": "int32"
                        },
                        "description": ""
                      },
                      "rem": {
                        "type": "array",
                        "items": {
                          "type": "integer",
                          "contentEncoding": "int32"
                        },
                        "description": ""
                      }
                    },
                    "examples": [
                      {
                        "add": [
                          182
                        ],
                        "rem": [
                          183
                        ]
                      }
                    ]
                  },
                  "group_assignees": {
                    "type": "object",
                    "properties": {
                      "add": {
                        "type": "array",
                        "items": {
                          "type": "string"
                        },
                        "description": ""
                      },
                      "rem": {
                        "type": "array",
                        "items": {
                          "type": "string"
                        },
                        "description": ""
                      }
                    }
                  },
                  "watchers": {
                    "title": "Watchers",
                    "required": [
                      "add",
                      "rem"
                    ],
                    "type": "object",
                    "properties": {
                      "add": {
                        "type": "array",
                        "items": {
                          "type": "integer",
                          "contentEncoding": "int32"
                        },
                        "description": ""
                      },
                      "rem": {
                        "type": "array",
                        "items": {
                          "type": "integer",
                          "contentEncoding": "int32"
                        },
                        "description": ""
                      }
                    },
                    "examples": [
                      {
                        "add": [
                          182,
                          121
                        ],
                        "rem": [
                          183,
                          122
                        ]
                      }
                    ]
                  },
                  "archived": {
                    "type": "boolean"
                  }
                },
                "examples": [
                  {
                    "name": "Updated Task Name",
                    "description": "Updated Task Content",
                    "status": "in progress",
                    "priority": 1,
                    "due_date": 1508369194377,
                    "due_date_time": false,
                    "parent": "abc1234",
                    "time_estimate": 8640000,
                    "start_date": 1567780450202,
                    "start_date_time": false,
                    "points": 3,
                    "assignees": {
                      "add": [
                        182
                      ],
                      "rem": [
                        183
                      ]
                    },
                    "group_assignees": {
                      "add": [
                        "dd01f92f-48ca-446d-88a1-0beb0e8f5f14"
                      ],
                      "rem": [
                        "dd01f92f-48ca-446d-88a1-0beb0e8f5f13"
                      ]
                    },
                    "watchers": {
                      "add": [
                        182
                      ],
                      "rem": [
                        183
                      ]
                    },
                    "archived": false
                  }
                ]
              },
              "example": {
                "name": "Updated Task Name",
                "description": "Updated Task Content",
                "status": "in progress",
                "priority": 3,
                "due_date": 1508369194377,
                "due_date_time": false,
                "parent": "abc1234",
                "time_estimate": 8640000,
                "start_date": 1567780450202,
                "start_date_time": false,
                "points": 3,
                "assignees": {
                  "add": [
                    182
                  ],
                  "rem": [
                    183
                  ]
                },
                "group_assignees": {
                  "add": [
                    "dd01f92f-48ca-446d-88a1-0beb0e8f5f14"
                  ],
                  "rem": [
                    "dd01f92f-48ca-446d-88a1-0beb0e8f5f13"
                  ]
                },
                "archived": false
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
                  "title": "UpdateTaskresponse",
                  "type": "object",
                  "properties": {
                    "id": {
                      "type": "string"
                    },
                    "custom_id": {
                      "type": [
                        "string",
                        "null"
                      ]
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
                    "text_content": {
                      "type": "string"
                    },
                    "description": {
                      "type": "string"
                    },
                    "status": {
                      "$ref": "#/paths/~1v2~1task~1%7Btask_id%7D/get/responses/200/content/application~1json/schema/properties/status"
                    },
                    "archived": {
                      "type": "boolean"
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
                    "group_assignees": {
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
                      "type": "string"
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
                        "string",
                        "null"
                      ]
                    },
                    "custom_fields": {
                      "type": "array",
                      "items": {
                        "title": "CustomFields7",
                        "required": [
                          "id",
                          "name",
                          "type",
                          "type_config",
                          "date_created",
                          "hide_from_guests",
                          "required"
                        ],
                        "type": "object",
                        "properties": {
                          "id": {
                            "type": "string"
                          },
                          "name": {
                            "type": "string"
                          },
                          "type": {
                            "type": "string"
                          },
                          "type_config": {
                            "$ref": "#/paths/~1v2~1task~1%7Btask_id%7D/get/responses/200/content/application~1json/schema/properties/custom_fields/items/properties/type_config"
                          },
                          "date_created": {
                            "type": "string"
                          },
                          "hide_from_guests": {
                            "type": "boolean"
                          },
                          "value": {
                            "type": "string"
                          },
                          "required": {
                            "type": "boolean"
                          }
                        },
                        "examples": [
                          {
                            "id": "0a52c486-5f05-403b-b4fd-c512ff05131c",
                            "name": "My Number field",
                            "type": "checkbox",
                            "type_config": {},
                            "date_created": "1622176979540",
                            "hide_from_guests": false,
                            "value": "23",
                            "required": true
                          }
                        ]
                      },
                      "description": ""
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
                      "custom_id": null,
                      "name": "Updated Task Name",
                      "text_content": "Updated Task Content",
                      "description": "Updated Task Content",
                      "status": {
                        "status": "in progress",
                        "color": "#d3d3d3",
                        "orderindex": 1,
                        "type": "custom"
                      },
                      "archived": false,
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
                      "group_assignees": [],
                      "checklists": [],
                      "tags": [],
                      "parent": "abc1234",
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
                      "custom_fields": [
                        {
                          "id": "0a52c486-5f05-403b-b4fd-c512ff05131c",
                          "name": "My Number field",
                          "type": "checkbox",
                          "type_config": {},
                          "date_created": "1622176979540",
                          "hide_from_guests": false,
                          "value": "23",
                          "required": true
                        },
                        {
                          "id": "03efda77-c7a0-42d3-8afd-fd546353c2f5",
                          "name": "My Text field",
                          "type": "short_text",
                          "type_config": {},
                          "date_created": "1622176979540",
                          "hide_from_guests": false,
                          "value": "Text field input",
                          "required": false
                        },
                        {
                          "id": "f4d2a20d-6759-4420-b853-222dbe2589d5",
                          "name": "My People",
                          "type": "users",
                          "type_config": {
                            "single_user": true,
                            "include_groups": true,
                            "include_guests": true,
                            "include_team_members": true
                          },
                          "date_created": "1618440378816",
                          "hide_from_guests": false,
                          "required": false
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
                "example": {
                  "id": "9hx",
                  "custom_id": null,
                  "custom_item_id": null,
                  "name": "Updated Task Name",
                  "text_content": "Updated Task Content",
                  "description": "Updated Task Content",
                  "markdown_description": "Updates Task Content",
                  "status": {
                    "status": "in progress",
                    "color": "#d3d3d3",
                    "orderindex": 1,
                    "type": "custom"
                  },
                  "archived": false,
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
                  "group_assignees": [],
                  "checklists": [],
                  "tags": [],
                  "parent": "abc1234",
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
                  "custom_fields": [
                    {
                      "id": "0a52c486-5f05-403b-b4fd-c512ff05131c",
                      "name": "My Number field",
                      "type": "checkbox",
                      "type_config": {},
                      "date_created": "1622176979540",
                      "hide_from_guests": false,
                      "value": "23",
                      "required": true
                    },
                    {
                      "id": "03efda77-c7a0-42d3-8afd-fd546353c2f5",
                      "name": "My Text field",
                      "type": "short_text",
                      "type_config": {},
                      "date_created": "1622176979540",
                      "hide_from_guests": false,
                      "value": "Text field input",
                      "required": false
                    },
                    {
                      "id": "f4d2a20d-6759-4420-b853-222dbe2589d5",
                      "name": "My People",
                      "type": "users",
                      "type_config": {
                        "single_user": true,
                        "include_groups": true,
                        "include_guests": true,
                        "include_team_members": true
                      },
                      "date_created": "1618440378816",
                      "hide_from_guests": false,
                      "required": false
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
      "name": "Tasks"
    }
  ]
}
```