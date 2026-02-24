# Create Task

Create a new task.

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
    "/v2/list/{list_id}/task": {
      "post": {
        "summary": "Create Task",
        "tags": [
          "Tasks"
        ],
        "description": "Create a new task.",
        "operationId": "CreateTask",
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
                "title": "CreateTaskrequest",
                "required": [
                  "name"
                ],
                "type": "object",
                "properties": {
                  "name": {
                    "type": "string"
                  },
                  "description": {
                    "type": "string"
                  },
                  "assignees": {
                    "type": "array",
                    "items": {
                      "type": "integer",
                      "contentEncoding": "int32"
                    },
                    "description": ""
                  },
                  "archived": {
                    "type": "boolean"
                  },
                  "group_assignees": {
                    "type": "array",
                    "items": {
                      "type": "string"
                    },
                    "description": "Assign multiple user groups to the task."
                  },
                  "tags": {
                    "type": "array",
                    "items": {
                      "type": "string"
                    },
                    "description": ""
                  },
                  "status": {
                    "type": "string"
                  },
                  "priority": {
                    "type": [
                      "integer",
                      "null"
                    ],
                    "contentEncoding": "int32"
                  },
                  "due_date": {
                    "type": "integer",
                    "contentEncoding": "int64"
                  },
                  "due_date_time": {
                    "type": "boolean"
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
                    "description": "Add Sprint Points to the task."
                  },
                  "notify_all": {
                    "type": "boolean",
                    "description": "If `notify_all` is true, notifications will be sent to everyone including the creator of the comment."
                  },
                  "parent": {
                    "description": "You can create a subtask by including an existing task ID.\\\n \\\nThe `parent` task ID you include can be a subtask, but must be in the same List specified in the path parameter.",
                    "type": [
                      "string",
                      "null"
                    ]
                  },
                  "markdown_content": {
                    "type": "string",
                    "description": "Markdown formatted description for the task. If both `markdown_content` and `description` are provided, `markdown_content` will be used instead of `description`."
                  },
                  "links_to": {
                    "description": "Include a task ID to create a linked dependency with your new task.",
                    "type": [
                      "string",
                      "null"
                    ]
                  },
                  "check_required_custom_fields": {
                    "description": "When creating a task via API any required Custom Fields are ignored by default (`false`).\\\n \\\nYou can enforce required Custom Fields by including `check_required_custom_fields: true`.",
                    "type": "boolean"
                  },
                  "custom_fields": {
                    "type": "array",
                    "items": {
                      "title": "SetCustomFieldValueOnCreateTaskrequest",
                      "anyOf": [
                        {
                          "type": "object",
                          "title": "URL Custom Field",
                          "description": "The `value` must be a string with a valid URL.",
                          "required": [
                            "id",
                            "value"
                          ],
                          "properties": {
                            "id": {
                              "type": "string"
                            },
                            "value": {
                              "type": [
                                "string",
                                "null"
                              ],
                              "example": "https://clickup.com/api"
                            }
                          }
                        },
                        {
                          "type": "object",
                          "title": "Dropdown Custom Field",
                          "description": "Enter the universal unique identifier (UUID) of the dropdown menu option you want to set. You can find the UUIDs available for each Dropdown Custom Field using [Get Accessible Custom Fields.](https://developer.clickup.com/reference/getaccessiblecustomfields) New Dropdown Custom Field options cannot be created from this request.",
                          "required": [
                            "id",
                            "value"
                          ],
                          "properties": {
                            "id": {
                              "type": "string"
                            },
                            "value": {
                              "type": [
                                "string",
                                "null"
                              ],
                              "example": "uuid1234"
                            }
                          }
                        },
                        {
                          "type": "object",
                          "title": "Email Custom Field",
                          "description": "The `value` must be a string with a valid email address.",
                          "required": [
                            "id",
                            "value"
                          ],
                          "properties": {
                            "id": {
                              "type": "string"
                            },
                            "value": {
                              "type": [
                                "string",
                                "null"
                              ],
                              "example": "user@company.com"
                            }
                          }
                        },
                        {
                          "type": "object",
                          "title": "Phone Custom Field",
                          "description": "The `value` must be a string with a valid country code.",
                          "required": [
                            "id",
                            "value"
                          ],
                          "properties": {
                            "id": {
                              "type": "string"
                            },
                            "value": {
                              "type": [
                                "string",
                                "null"
                              ],
                              "example": "+1 123 456 7890"
                            }
                          }
                        },
                        {
                          "type": "object",
                          "title": "Date Custom Field",
                          "description": "The `value` must be Unix time in milliseconds. To display the time in a Date Custom Field in ClickUp, you must include `time: true` in the `value_options` property.",
                          "required": [
                            "id",
                            "value"
                          ],
                          "properties": {
                            "id": {
                              "type": "string"
                            },
                            "value": {
                              "type": [
                                "integer",
                                "null"
                              ],
                              "format": "int64",
                              "example": 1667367645000
                            },
                            "value_options": {
                              "type": "object",
                              "properties": {
                                "time": {
                                  "type": "boolean",
                                  "example": true
                                }
                              }
                            }
                          }
                        },
                        {
                          "type": "object",
                          "title": "Short or Long Text Custom Field",
                          "description": "Enter a string of text.",
                          "required": [
                            "id",
                            "value"
                          ],
                          "properties": {
                            "id": {
                              "type": "string"
                            },
                            "value": {
                              "type": [
                                "string",
                                "null"
                              ],
                              "example": "This is short or long text in a Custom Field."
                            }
                          }
                        },
                        {
                          "type": "object",
                          "title": "Number Custom Field",
                          "description": "Enter a number.",
                          "required": [
                            "id",
                            "value"
                          ],
                          "properties": {
                            "id": {
                              "type": "string"
                            },
                            "value": {
                              "type": [
                                "number",
                                "null"
                              ],
                              "example": -28
                            }
                          }
                        },
                        {
                          "type": "object",
                          "title": "Money Custom Field",
                          "description": "You can set an amount, but not the currency of a Money Custom Field via the API. You can check the currency of a Money Custom Field using [Get Accessible Custom Fields.](https://developer.clickup.com/reference/getaccessiblecustomfields)",
                          "required": [
                            "id",
                            "value"
                          ],
                          "properties": {
                            "id": {
                              "type": "string"
                            },
                            "value": {
                              "type": [
                                "number",
                                "null"
                              ],
                              "example": 8000
                            }
                          }
                        },
                        {
                          "type": "object",
                          "title": "Task Relationship Custom Field",
                          "description": "Enter an array of task ids in the `add` property to add them to a Task Relationship Custom Field. Enter them into the `rem` property to remove tasks from the Relationship. Task Relationship Custom Fields are nullable: `\"value\": null`.",
                          "required": [
                            "id",
                            "value"
                          ],
                          "properties": {
                            "id": {
                              "type": "string"
                            },
                            "value": {
                              "type": "object",
                              "properties": {
                                "add": {
                                  "type": "array",
                                  "items": {
                                    "type": "string"
                                  }
                                },
                                "rem": {
                                  "type": "array",
                                  "items": {
                                    "type": "string"
                                  }
                                }
                              }
                            }
                          }
                        },
                        {
                          "type": "object",
                          "title": "People Custom Field",
                          "description": "Enter an array of user ids or a Team id in the `add` property to add them to a People Custom Field. Enter them into the `rem` property to remove users from a People Custom Field. You can get a list of people in the Workspace using [Get Authorized Teams (Workspaces).](https://developer.clickup.com/reference/getauthorizedteams) People Custom Fields are nullable: `\"value\": null`.",
                          "required": [
                            "id",
                            "value"
                          ],
                          "properties": {
                            "id": {
                              "type": "string"
                            },
                            "value": {
                              "type": "object",
                              "properties": {
                                "add": {
                                  "type": "array",
                                  "items": {
                                    "type": "number"
                                  }
                                },
                                "rem": {
                                  "type": "array",
                                  "items": {
                                    "type": "number"
                                  }
                                }
                              }
                            }
                          }
                        },
                        {
                          "type": "object",
                          "title": "Emoji (Rating) Custom Field",
                          "description": "Enter an integer that is greater than or equal to zero and where the `count` property is greater than or equal to the `value`. You can find the `count` property for each Emoji (Rating) Custom Field using [Get Accessible Custom Fields.](https://developer.clickup.com/reference/getaccessiblecustomfields)",
                          "required": [
                            "id",
                            "value"
                          ],
                          "properties": {
                            "id": {
                              "type": "string"
                            },
                            "value": {
                              "type": [
                                "integer",
                                "null"
                              ],
                              "format": "int32",
                              "example": 4
                            }
                          }
                        },
                        {
                          "type": "object",
                          "title": "Manual Progress Custom Field",
                          "description": "Enter a number between the `start` and `end` values of each Manual Progress Custom Field. For example, for a field with `start: 10` and `end: 30`, sending `current: 20` will be displayed as 50% complete in ClickUp. You can find the `start` and `end` values for each Manual Progress Custom Field using [Get Accessible Custom Fields.](https://developer.clickup.com/reference/getaccessiblecustomfields) Manual Progress Custom Fields are nullable: `\"value\": null`.",
                          "required": [
                            "id",
                            "value"
                          ],
                          "properties": {
                            "id": {
                              "type": "string"
                            },
                            "value": {
                              "type": "object",
                              "required": [
                                "current"
                              ],
                              "properties": {
                                "current": {
                                  "type": "number",
                                  "example": 20
                                }
                              }
                            }
                          }
                        },
                        {
                          "type": "object",
                          "title": "Label Custom Field",
                          "description": "Enter an array of the universal unique identifiers (UUIDs) of the labels you want to apply. You can find the UUIDs available for each Label Custom Field using [Get Accessible Custom Fields.](https://developer.clickup.com/reference/getaccessiblecustomfields) Label Custom Fields are nullable: `\"value\": null`.",
                          "required": [
                            "id",
                            "value"
                          ],
                          "properties": {
                            "id": {
                              "type": "string"
                            },
                            "value": {
                              "type": "array",
                              "items": {
                                "type": "string",
                                "example": [
                                  "uuid1234",
                                  "uuid9876"
                                ]
                              }
                            }
                          }
                        },
                        {
                          "type": "object",
                          "title": "Location Custom Field",
                          "description": "Include the latitude, longitude, and formatted address as defined in the [Google Maps Geocoding API.](https://developers.google.com/maps/documentation/geocoding/overview)",
                          "required": [
                            "id",
                            "value"
                          ],
                          "properties": {
                            "id": {
                              "type": "string"
                            },
                            "value": {
                              "type": "object",
                              "properties": {
                                "location": {
                                  "type": "object",
                                  "properties": {
                                    "lat": {
                                      "type": "number"
                                    },
                                    "lng": {
                                      "type": "number"
                                    }
                                  }
                                },
                                "formatted_address": {
                                  "type": "string"
                                }
                              }
                            }
                          }
                        },
                        {
                          "type": "object",
                          "title": "Button Custom Field",
                          "description": "Set a button Custom Field to `true` to \"click\" it. This will trigger the button's action as if it was clicked in the UI.",
                          "required": [
                            "id",
                            "value"
                          ],
                          "properties": {
                            "id": {
                              "type": "string"
                            },
                            "value": {
                              "type": [
                                "boolean",
                                "null"
                              ],
                              "example": true
                            }
                          }
                        }
                      ]
                    },
                    "description": "You can include one or more Custom Fields to set them when creating a new task.\\\n \\\nCustom Fields that use object and array type values are nullable by sending `\"value\": null`."
                  },
                  "custom_item_id": {
                    "type": "number",
                    "description": "The custom task type ID for this task. A value of `null` (default) creates a standard task type \"Task\".\\\n \\\nTo get a list of available custom task type IDs for your Workspace, use the [Get Custom Task Types endpoint](https://developer.clickup.com/reference/getcustomitems)."
                  }
                },
                "examples": [
                  {
                    "name": "New Task Name",
                    "description": "New Task Description",
                    "assignees": [
                      183
                    ],
                    "archived": false,
                    "group_assignees": [
                      "dd01f92f-48ca-446d-88a1-0beb0e8f5f14"
                    ],
                    "tags": [
                      "tag name 1"
                    ],
                    "status": "Open",
                    "priority": 3,
                    "due_date": 1508369194377,
                    "due_date_time": false,
                    "time_estimate": 8640000,
                    "start_date": 1567780450202,
                    "start_date_time": false,
                    "points": 3,
                    "notify_all": true,
                    "parent": null,
                    "links_to": null,
                    "check_required_custom_fields": true,
                    "custom_fields": [
                      {
                        "id": "0a52c486-5f05-403b-b4fd-c512ff05131c",
                        "value": 23
                      },
                      {
                        "id": "03efda77-c7a0-42d3-8afd-fd546353c2f5",
                        "value": "Text field input"
                      }
                    ]
                  }
                ]
              },
              "example": {
                "name": "New Task Name",
                "description": "New Task Description",
                "markdown_description": "New Task Description",
                "assignees": [
                  183
                ],
                "archived": false,
                "group_assignees": [
                  "dd01f92f-48ca-446d-88a1-0beb0e8f5f14"
                ],
                "email_assignees": [
                  "dd01f92f-48ca-446d-88a1-0beb0e8f5f13"
                ],
                "tags": [
                  "tag name 1"
                ],
                "status": "Open",
                "priority": 3,
                "due_date": 1508369194377,
                "due_date_time": false,
                "time_estimate": 8640000,
                "start_date": 1567780450202,
                "start_date_time": false,
                "points": 3,
                "notify_all": true,
                "parent": null,
                "links_to": null,
                "check_required_custom_fields": true,
                "custom_fields": [
                  {
                    "id": "0a52c486-5f05-403b-b4fd-c512ff05131c",
                    "value": "This is a string of text added to a Custom Field."
                  }
                ]
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
                  "title": "CreateTaskresponse.yaml",
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
                      ],
                      "description": "The custom task type ID for this task. A value of `null` (default) creates a standard task type \"Task\".\\\n \\\nTo get a list of available custom task type IDs for your Workspace, use the [Get Custom Task Types endpoint](https://developer.clickup.com/reference/getcustomitems)."
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
                    "archived": {
                      "type": "boolean"
                    },
                    "group_assignees": {
                      "type": "array",
                      "items": {
                        "type": "string"
                      },
                      "description": ""
                    },
                    "email_assignees": {
                      "type": "string"
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
                        "string",
                        "null"
                      ]
                    },
                    "custom_fields": {
                      "type": "array",
                      "items": {
                        "$ref": "#/paths/~1v2~1task~1%7Btask_id%7D/get/responses/200/content/application~1json/schema/properties/custom_fields/items"
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
                  }
                },
                "example": {
                  "id": "9hx",
                  "custom_id": null,
                  "custom_item_id": null,
                  "name": "New Task Name",
                  "text_content": "New Task Content",
                  "description": "New Task Content",
                  "markdown_description": "New Task Content",
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
                  "date_done": null,
                  "creator": {
                    "id": 183,
                    "username": "John Doe",
                    "color": "#827718",
                    "profilePicture": "https://attachments-public.clickup.com/profilePictures/183_abc.jpg"
                  },
                  "assignees": [],
                  "archived": false,
                  "group_assignees": [],
                  "email_assignees": [],
                  "checklists": [],
                  "tags": [],
                  "parent": "abc1234",
                  "priority": {
                    "color": "6fddff",
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
                      "name": "My Text Custom field",
                      "type": "text",
                      "type_config": {},
                      "date_created": "1622176979540",
                      "hide_from_guests": false,
                      "value": {
                        "value": "This is a string of text added to a Custom Field."
                      },
                      "required": true
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