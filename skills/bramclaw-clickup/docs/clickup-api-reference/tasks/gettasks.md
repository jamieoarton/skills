# Get Tasks

View the tasks in a List. Responses are limited to 100 tasks per page. You can only view task information of tasks you can access. \
 \
This endpoint only includes tasks where the specified `list_id` is their home List. Tasks added to the `list_id` with a different home List are not included in the response by default. To include tasks that exist in multiple lists, use the `include_timl` parameter. \
 \
The `time_spent` field displays time tracked in milliseconds, and is only included in the response for tasks with time entries.

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
      "get": {
        "summary": "Get Tasks",
        "tags": [
          "Tasks"
        ],
        "description": "View the tasks in a List. Responses are limited to 100 tasks per page. You can only view task information of tasks you can access. \\\n \\\nThis endpoint only includes tasks where the specified `list_id` is their home List. Tasks added to the `list_id` with a different home List are not included in the response by default. To include tasks that exist in multiple lists, use the `include_timl` parameter. \\\n \\\nThe `time_spent` field displays time tracked in milliseconds, and is only included in the response for tasks with time entries.",
        "operationId": "GetTasks",
        "parameters": [
          {
            "name": "list_id",
            "in": "path",
            "description": "To find the list_id: \\ 1. In the Sidebar, hover over the List and click the **ellipsis ...** menu. \\ 2. Select **Copy link.** \\ 3. Use the copied URL to find the list_id. The list_id is the number that follows /li in the URL.",
            "required": true,
            "style": "simple",
            "schema": {
              "type": "number",
              "contentEncoding": "double",
              "examples": [
                123
              ]
            }
          },
          {
            "name": "archived",
            "in": "query",
            "description": "",
            "style": "form",
            "explode": true,
            "schema": {
              "type": "boolean",
              "examples": [
                false
              ]
            }
          },
          {
            "name": "include_markdown_description",
            "in": "query",
            "description": "To return task descriptions in Markdown format, use `?include_markdown_description=true`.",
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
            "name": "page",
            "in": "query",
            "description": "Page to fetch (starts at 0).",
            "style": "form",
            "explode": true,
            "schema": {
              "type": "integer",
              "contentEncoding": "int32"
            }
          },
          {
            "name": "order_by",
            "in": "query",
            "description": "Order by a particular field. By default, tasks are ordered by `created`.\\\n \\\nOptions include: `id`, `created`, `updated`, and `due_date`.",
            "style": "form",
            "explode": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "reverse",
            "in": "query",
            "description": "Tasks are displayed in reverse order.",
            "style": "form",
            "explode": true,
            "schema": {
              "type": "boolean"
            }
          },
          {
            "name": "subtasks",
            "in": "query",
            "description": "Include or exclude subtasks. By default, subtasks are excluded.",
            "style": "form",
            "explode": true,
            "schema": {
              "type": "boolean"
            }
          },
          {
            "name": "statuses",
            "in": "query",
            "description": "Filter by statuses. To include closed tasks, use the `include_closed` parameter. \\\n \\\nFor example: \\\n \\\n`?statuses[]=to%20do&statuses[]=in%20progress`",
            "style": "form",
            "explode": true,
            "schema": {
              "type": "array",
              "items": {
                "type": "string"
              }
            }
          },
          {
            "name": "include_closed",
            "in": "query",
            "description": "Include or excluse closed tasks. By default, they are excluded.\\\n \\\nTo include closed tasks, use `include_closed: true`.",
            "style": "form",
            "explode": true,
            "schema": {
              "type": "boolean"
            }
          },
          {
            "name": "include_timl",
            "in": "query",
            "description": "Include Tasks in Multiple Lists. By default, tasks that exist in multiple lists are excluded from the response.\\\n \\\nTo include tasks that exist in multiple lists, use `include_timl: true`.",
            "style": "form",
            "explode": true,
            "schema": {
              "type": "boolean"
            }
          },
          {
            "name": "assignees",
            "in": "query",
            "description": "Filter by Assignees. For example: \\\n \\\n`?assignees[]=1234&assignees[]=5678`",
            "style": "form",
            "explode": true,
            "schema": {
              "type": "array",
              "items": {
                "type": "string"
              }
            }
          },
          {
            "name": "watchers",
            "in": "query",
            "description": "Filter by watchers.",
            "style": "form",
            "explode": true,
            "schema": {
              "type": "array",
              "items": {
                "type": "string"
              }
            }
          },
          {
            "name": "tags",
            "in": "query",
            "description": "Filter by tags. For example: \\\n \\\n`?tags[]=tag1&tags[]=this%20tag`",
            "style": "form",
            "explode": true,
            "schema": {
              "type": "array",
              "items": {
                "type": "string"
              }
            }
          },
          {
            "name": "due_date_gt",
            "in": "query",
            "description": "Filter by due date greater than Unix time in milliseconds.",
            "style": "form",
            "explode": true,
            "schema": {
              "type": "integer",
              "contentEncoding": "int32"
            }
          },
          {
            "name": "due_date_lt",
            "in": "query",
            "description": "Filter by due date less than Unix time in milliseconds.",
            "style": "form",
            "explode": true,
            "schema": {
              "type": "integer",
              "contentEncoding": "int32"
            }
          },
          {
            "name": "date_created_gt",
            "in": "query",
            "description": "Filter by date created greater than Unix time in milliseconds.",
            "style": "form",
            "explode": true,
            "schema": {
              "type": "integer",
              "contentEncoding": "int32"
            }
          },
          {
            "name": "date_created_lt",
            "in": "query",
            "description": "Filter by date created less than Unix time in milliseconds.",
            "style": "form",
            "explode": true,
            "schema": {
              "type": "integer",
              "contentEncoding": "int32"
            }
          },
          {
            "name": "date_updated_gt",
            "in": "query",
            "description": "Filter by date updated greater than Unix time in milliseconds.",
            "style": "form",
            "explode": true,
            "schema": {
              "type": "integer",
              "contentEncoding": "int32"
            }
          },
          {
            "name": "date_updated_lt",
            "in": "query",
            "description": "Filter by date updated less than Unix time in milliseconds.",
            "style": "form",
            "explode": true,
            "schema": {
              "type": "integer",
              "contentEncoding": "int32"
            }
          },
          {
            "name": "date_done_gt",
            "in": "query",
            "description": "Filter by date done greater than Unix time in milliseconds.",
            "style": "form",
            "explode": true,
            "schema": {
              "type": "integer",
              "contentEncoding": "int32"
            }
          },
          {
            "name": "date_done_lt",
            "in": "query",
            "description": "Filter by date done less than Unix time in milliseconds.",
            "style": "form",
            "explode": true,
            "schema": {
              "type": "integer",
              "contentEncoding": "int32"
            }
          },
          {
            "name": "custom_fields",
            "in": "query",
            "description": "Include tasks with specific values in one or more Custom Fields. Custom Relationships are included.\\\n \\\nFor example: `?custom_fields=[{\"field_id\":\"abcdefghi12345678\",\"operator\":\"=\",\"value\":\"1234\"},{\"field_id\":\"jklmnop123456\",\"operator\":\"<\",\"value\":\"5\"}]`\\\n \\\nOnly set Custom Field values display in the `value` property of the `custom_fields` parameter. If you want to include tasks with specific values in only one Custom Field, use `custom_field` instead.\\\n \\\nLearn more about [filtering using Custom Fields.](https://developer.clickup.com/docs/taskfilters)",
            "style": "form",
            "explode": true,
            "schema": {
              "type": "array",
              "items": {
                "type": "string"
              }
            }
          },
          {
            "name": "custom_field",
            "in": "query",
            "description": "Include tasks with specific values in only one Custom Field. This Custom Field can be a Custom Relationship.",
            "style": "form",
            "explode": true,
            "schema": {
              "type": "array",
              "items": {
                "type": "string"
              }
            }
          },
          {
            "name": "custom_items",
            "in": "query",
            "description": "Filter by custom task types. For example: \\\n \\\n`?custom_items[]=0&custom_items[]=1300` \\\n \\\nIncluding `0` returns tasks. Including `1` returns Milestones. Including any other number returns the custom task type as defined in your Workspace.",
            "style": "form",
            "explode": true,
            "schema": {
              "type": "array",
              "items": {
                "type": "number"
              }
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
                  "example": [
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
                          "watchers": [],
                          "checklists": [],
                          "tags": [],
                          "parent": null,
                          "priority": {
                            "color": "#f8ae00",
                            "id": "2",
                            "orderindex": "2",
                            "priority": "high"
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
                          "watchers": [],
                          "checklists": [],
                          "tags": [],
                          "parent": null,
                          "priority": null,
                          "due_date": null,
                          "points": 3,
                          "time_estimate": null,
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
                      ]
                    }
                  ],
                  "title": "GetTasksresponse",
                  "type": "object",
                  "properties": {
                    "tasks": {
                      "type": "array",
                      "items": {
                        "title": "TaskWithMixedOrderIndexType",
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
                            "type": [
                              "string",
                              "number"
                            ]
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
                          "custom_item_id": null,
                          "name": "New Task Name",
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
                          "checklists": {
                            "id": "595495f8-4557-41b7-a527-f808664816a0",
                            "task_id": "86cv5pkvr",
                            "name": "Checklist on a task",
                            "date_created": "1714661812846",
                            "orderindex": "1",
                            "creator": 2770032,
                            "resolved": 0,
                            "unresolved": 2,
                            "items": []
                          },
                          "tags": [],
                          "parent": null,
                          "priority": {
                            "color": "#f8ae00",
                            "id": "2",
                            "orderindex": "2",
                            "priority": "high"
                          },
                          "due_date": null,
                          "start_date": null,
                          "points": 3,
                          "time_estimate": null,
                          "time_spent": 7200000,
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
                          "custom_item_id": null,
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
                          "watchers": [],
                          "checklists": {
                            "id": "de159781-452c-4ef3-a3ac-0df4bf18aae2",
                            "name": "Checklist item 1",
                            "orderindex": 0,
                            "assignee": null,
                            "group_assignee": null,
                            "resolved": false,
                            "parent": null,
                            "date_created": "1714661817234",
                            "children": []
                          },
                          "tags": [],
                          "parent": null,
                          "priority": null,
                          "due_date": null,
                          "start_date": null,
                          "points": 3,
                          "time_estimate": null,
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
                      ]
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
      "name": "Tasks"
    }
  ]
}
```